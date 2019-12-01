FROM python:3-alpine
WORKDIR /app
COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/apperator
ENTRYPOINT ["python3", "/app/apperator/run.py"]
