FROM python:3
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
#ENTRYPOINT [ "python", "-u", "main.py" ]
ENTRYPOINT ["gunicorn", "-w", "1", "bonsai:app"]