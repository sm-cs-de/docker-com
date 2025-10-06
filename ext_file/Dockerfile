FROM python:3.13.7-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ext_file.py .

CMD ["python", "ext_file.py"]

