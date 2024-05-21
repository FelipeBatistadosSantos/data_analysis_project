FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt setup.py /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["python", "src/main.py"]
