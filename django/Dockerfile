FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /server
ADD requirements.txt /server/
RUN pip install -r requirements.txt
ADD . /server/
