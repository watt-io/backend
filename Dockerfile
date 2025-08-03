# Usar imagem oficial do Python
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivo de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Tornar o script executável
RUN chmod +x start.sh

# Expor porta 8000
EXPOSE 8000

# Comando para executar a aplicação
CMD ["./start.sh"]

# Comando alternativo para executar testes
# CMD ["pytest", "-v"] 