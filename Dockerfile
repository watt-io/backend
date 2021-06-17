FROM python:3.8.5-slim-buster

COPY ./src /backend/src

WORKDIR /backend

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


EXPOSE 8000

CMD [ "uvicorn", "src.server:app","--host=0.0.0.0", "--reload" ]