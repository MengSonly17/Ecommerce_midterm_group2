# Use Python 3.13.2 slim image
FROM python:3.13.2-slim

# Prevent Python from writing pyc files & buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (PostgreSQL + MySQL client build tools)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && apt-get clean

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run Django app via Gunicorn
CMD ["gunicorn", "EcommerceMidterm.wsgi:application", "--bind", "0.0.0.0:9000"]
