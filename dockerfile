# Use uma imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos requirements.txt e setup.py para o diretório de trabalho
COPY requirements.txt setup.py /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . /app/

# Instale o pacote usando setup.py
RUN pip install --no-cache-dir -e .

# Exponha a porta que o Flask usará (caso esteja usando Flask)
EXPOSE 5000

# Comando padrão para rodar a aplicação
CMD ["python", "src/main.py"]
