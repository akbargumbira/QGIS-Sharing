FROM kartoza/django-base
MAINTAINER Akbar Gumbira <akbargumbira@gmail.com>

COPY REQUIREMENTS.txt /REQUIREMENTS.txt
RUN pip install -r /REQUIREMENTS.txt
ENV PYTHONUNBUFFERED 1

WORKDIR /home/web/django_project
