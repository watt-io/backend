#!/bin/bash

# Criar diretório de dados se não existir
mkdir -p /app/data

# Executar migrações do Alembic
echo "Executando migrações do banco de dados..."
alembic upgrade head

# Iniciar a aplicação
echo "Iniciando a aplicação..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 