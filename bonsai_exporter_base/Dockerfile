FROM python:3.9
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt

LABEL name="bonsai_exporter_base"

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD timeout 5 cat /proc/1/fd/2 | grep -q "Recv: 200"

#ENTRYPOINT [ "python", "-u", "main.py" ]
ENTRYPOINT ["/opt/entrypoint.sh"]