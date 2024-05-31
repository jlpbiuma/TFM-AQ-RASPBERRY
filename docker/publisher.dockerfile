FROM python:3.9-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./publisher.py .

CMD ["python", "-u", "publisher.py"]
