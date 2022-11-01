FROM python:3.9
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "-u", "main.py" ]
#ENTRYPOINT ["gunicorn", "-w", "1", "--bind", "0.0.0.0:4000", "bonsai:app"]