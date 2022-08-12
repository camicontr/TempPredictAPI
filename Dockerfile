# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY main.py /app
COPY requirements.txt /app
COPY model /app/model
COPY ms /app/ms

# Install dependencies
RUN pip install -r requirements.txt
