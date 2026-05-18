#!/bin/sh
set -e

echo "Aguardando PostgreSQL..."
until pg_isready -h db -p 5432 -U "${POSTGRES_USER}" > /dev/null 2>&1; do
  sleep 1
done
echo "PostgreSQL disponível."

echo "Executando migrations..."
alembic upgrade head

echo "Iniciando aplicação..."
exec "$@"
