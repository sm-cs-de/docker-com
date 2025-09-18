FROM python:3.13.7-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py .

# Enhanced options - otherwise the messages do not appear
CMD ["python", "-u", "-m", "consumer.py"]
