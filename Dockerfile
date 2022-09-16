FROM python
COPY ./requirements.txt /app/requirements.txt
COPY ./sql_app /app/sql_app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8000