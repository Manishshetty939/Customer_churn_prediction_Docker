# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files in api/ folder to /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
