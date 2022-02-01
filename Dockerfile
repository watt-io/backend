FROM python:3.9-slim

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

COPY ./src ./src
COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", "--reload" ]