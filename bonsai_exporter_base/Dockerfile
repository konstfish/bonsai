FROM python:3.9
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt

LABEL name="bonsai_exporter_base"

#ENTRYPOINT [ "python", "-u", "main.py" ]
ENTRYPOINT ["/opt/entrypoint.sh"]