FROM ubuntu:18.04

MAINTAINER Lenny Kamande "lennymanyeki@gmail.com"

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y nginx uwsgi uwsgi-plugin-python3

COPY ./Requirements.txt /Requirements.txt
COPY ./nginx.conf /etc/nginx/nginx.conf


WORKDIR /

RUN pip3 install -r Requirements.txt

COPY . /

RUN adduser --disabled-password --gecos '' nginx\  
  && chown -R nginx:nginx /app \
  && chmod 777 /run/ -R \
  && chmod 777 /root/ -R

ENTRYPOINT [ "/bin/bash", "/launcher.sh"] 

EXPOSE 5000