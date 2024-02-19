# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para o diretório de trabalho do contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para executar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
