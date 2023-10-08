FROM python:3.9

WORKDIR /opt

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /opt

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD timeout 5 cat /proc/1/fd/2 | grep -q "Recv: 200"

ENV IN_DOCKER_CONTAINER 1
LABEL name="bonsai_exporter_base"

ENTRYPOINT ["/opt/entrypoint.sh"]
#ENTRYPOINT [ "python", "-u", "main.py" ]