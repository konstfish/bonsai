FROM python:3.9
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD python3 health.py

LABEL name="bonsai_server"

ENTRYPOINT [ "python", "-u", "bonsai.py" ]
#ENTRYPOINT ["gunicorn", "-w", "1", "--bind", "0.0.0.0:4000", "bonsai:app"]