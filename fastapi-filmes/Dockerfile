# Use imagem oficial do Python 3.11 (ou outra versão compatível)
FROM python:3.11-slim

# Defina diretório de trabalho no container
WORKDIR /app

# Copie arquivos de dependências
COPY requirements.txt .

# Instale dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código
COPY . .

# Exponha a porta que a FastAPI vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
