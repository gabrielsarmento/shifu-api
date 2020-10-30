FROM python:3.8.5

WORKDIR /shifu

ADD ./ ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD gunicorn -w 4 -b 0.0.0.0:8080 'main:create_app()'