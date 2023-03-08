#!/bin/bash
set -e

if [[ -d "/opt/custom_exporters" ]]; then
    echo "[*] Copying custom exporters"
    cp /opt/custom_exporters/* /opt/exporters/
fi

while IFS=',' read -ra ADDR; do
    for i in "${ADDR[@]}"; do
        echo "[*] Installing $i"
        pip --no-input install $i
    done
done <<< "$PIP_INSTALL"

exec python -u main.py "$@"

exec "$@"