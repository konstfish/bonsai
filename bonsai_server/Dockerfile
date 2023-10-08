FROM python:3.9

WORKDIR /opt

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /opt

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD python3 health.py

ENV IN_DOCKER_CONTAINER 1
LABEL name="bonsai_server"

ENTRYPOINT [ "python", "-u", "bonsai.py" ]
#ENTRYPOINT ["gunicorn", "-w", "1", "--bind", "0.0.0.0:4000", "bonsai:app"]