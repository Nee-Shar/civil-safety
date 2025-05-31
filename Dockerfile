# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR .

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default FastAPI port
EXPOSE 8000

# Start both FastAPI and Telegram bot
CMD ["python", "run_all.py"]
