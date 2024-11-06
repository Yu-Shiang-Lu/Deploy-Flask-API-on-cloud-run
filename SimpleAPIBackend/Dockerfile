FROM python:3.12-slim
LABEL authors="luyuxiang"
WORKDIR SimpleAPIBackend/app
COPY SimpleAPIBackend/requirements.txt .
COPY SimpleAPIBackend/app .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]