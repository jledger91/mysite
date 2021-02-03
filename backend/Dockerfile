FROM python:3.8-slim

RUN apt-get update

RUN mkdir /django

ADD src /django/src
ADD requirements/ /django/requirements

ARG DEPLOYMENT_ENVIRONMENT
RUN pip3 install -r /django/requirements/${DEPLOYMENT_ENVIRONMENT}.txt

WORKDIR /django/src

CMD ["/usr/local/bin/gunicorn","project.wsgi:application","-b","0.0.0.0:8000","-w","4","-t","600"]
