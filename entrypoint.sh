#!/bin/sh
set -e

echo "Esperando o banco de dados ficar pronto..."
/wait-for-it.sh database:3306 --timeout=60 --strict -- echo "Banco de dados pronto!"

echo "Rodando seeders..."
python3 -m app.seeders.seed

echo "Iniciando uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8090 --reload
