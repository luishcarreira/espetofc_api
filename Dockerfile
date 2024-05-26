# Use a imagem base oficial do Python
FROM python:3.12-slim

# Instalar Poetry
RUN pip install poetry

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock* ./

# Instalar dependências do Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copiar o restante dos arquivos do projeto
COPY . .

# Definir variáveis de ambiente
ENV PYTHONPATH=/app

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
