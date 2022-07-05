FROM python:3

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/local/scavenger

WORKDIR /usr/local/scavenger

COPY . /usr/local/scavenger/

RUN pip install -r requirements.txt

ENTRYPOINT python manage.py runserver 0.0.0.0:8000

# docker build -t scavenger:1.0.0 .
# docker login
# docker tag scavenger:1.0.0 shiyang19822000/scavenger:1.0.0
# docker push shiyang19822000/scavenger:1.0.0
