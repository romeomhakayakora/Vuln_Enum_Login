# Use a lightweight Python 3.12 base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

