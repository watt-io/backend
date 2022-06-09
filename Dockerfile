FROM python
WORKDIR /backend
COPY ./requirements.txt .
COPY ./filmes.db .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000