FROM python:3.9

WORKDIR /opt/app

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update 
RUN apt-get install tar

RUN tar zxfv data.tgz
