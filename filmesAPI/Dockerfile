FROM python:3.8-slim-buster

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /usr/src/app

# EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]