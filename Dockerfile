FROM python:3.4

RUN  apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean

WORKDIR /app
COPY requirements.txt requirements.txt
COPY run.sh run.sh
COPY scripts scripts

RUN apt-get install p7zip p7zip-full unzip
RUN pip install -r requirements.txt

CMD ["bash", "run.sh"]
