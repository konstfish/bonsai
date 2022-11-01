FROM python:3.9
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "-u", "main.py" ]