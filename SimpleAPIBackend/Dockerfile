FROM python:3.12-slim
LABEL authors="luyuxiang"
WORKDIR /app
COPY requirements.txt .
COPY app .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]