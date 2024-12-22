FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install uwsgi
# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirement.txt .
RUN  pip install -r requirement.txt
# Copy the application files
COPY . .

# Expose the app port
EXPOSE 5000

# Run uWSGI with minimal configuration
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--module", "app:app"]
