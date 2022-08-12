# Base image
FROM python:3.9.7

# Set working directory
WORKDIR /app

# Copy files
COPY main.py /app
COPY requirements.txt /app
COPY model /app/model
COPY ms /app/ms

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--port", "8000"]