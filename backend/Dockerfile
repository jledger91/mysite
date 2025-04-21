FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    tox \
    postgresql

RUN mkdir /django

ADD src /django/src
ADD requirements/ /django/requirements

ARG DEPLOYMENT_ENVIRONMENT
RUN pip install --upgrade pip
RUN pip install -r /django/requirements/${DEPLOYMENT_ENVIRONMENT}.txt

WORKDIR /django/src

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn","config.wsgi:application","-b","0.0.0.0:8000","-w","4","-t","600"]
