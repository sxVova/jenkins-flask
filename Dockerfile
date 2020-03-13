FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./application.py  /app/application.py
COPY ./static/ /app/static/
COPY ./templates/ /app/templates/
COPY ./roles/flask_role/files/.env /app/.env
   

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]