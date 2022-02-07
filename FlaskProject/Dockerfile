# FROM python:3.8.9
# COPY . /main
# WORKDIR /main
# RUN pip install -r requirements.txt
# ENTRYPOINT [ "python" ]
# CMD [ "main.py" ]









FROM python:3.8.9

ENV PYTHONUNBUFFERED 1

WORKDIR /main

ADD . /main

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /main
