FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt /app

WORKDIR /app

RUN pip install --upgrade pip \
	&& pip install --trusted-host pypi.python.org --requirement requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]