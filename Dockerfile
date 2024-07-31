FROM python:3.10-alpine3.20
LABEL maintainer="melnikalex2014@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/
RUN pip install Pillow
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

USER my_user
