# Use the official lightweight Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port Flask runs on
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
