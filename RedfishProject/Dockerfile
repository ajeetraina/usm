FROM python:2.7


RUN pip install Django==1.8 requests

ADD . /mydjango-app

WORKDIR /mydjango-app

CMD [ "python", "./manage.py syncdb" ]

CMD [ "python", "./manage.py migrate" ]

CMD [ "python", "./manage.py runserver 100.98.26.42:8000" ]
