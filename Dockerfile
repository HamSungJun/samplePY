FROM jenkins:latest
USER root
RUN apt-get update
RUN apt-get dist-upgrade
RUN apt-get install python3
RUN apt-get install python3-pip
RUN pip3 install --upgrade pip
RUN apt-get install pylint