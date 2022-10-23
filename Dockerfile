FROM python

COPY ./requirements.txt /src/requirements.txt

COPY ./app /src/app 

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

WORKDIR /src

EXPOSE 8000