FROM python:3.8-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /usr/local/src/get_smule
WORKDIR $APP_HOME

COPY src/ .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --timeout 0 runme:app
