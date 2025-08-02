# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose port and run
EXPOSE 5000
CMD ["python", "app.py"]
