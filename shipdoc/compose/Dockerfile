FROM python:3
RUN mkdir /code && apt-get update && apt-get -y upgrade && apt -y autoremove
COPY ./code /code
WORKDIR /code
RUN pip install -r /code/requirements.txt