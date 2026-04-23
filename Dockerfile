# Usa uma imagem oficial do Python, versão slim para ser mais leve
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro (otimiza o cache do Docker)
COPY requirements.txt .

# Atualiza o pip e instala as dependências sem guardar cache para reduzir tamanho da imagem
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para dentro do container
COPY . .

# Expõe a porta 8000 que será usada pelo FastAPI
EXPOSE 8000

# Comando para rodar a aplicação usando o uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]