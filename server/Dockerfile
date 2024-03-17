FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 50051

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]

