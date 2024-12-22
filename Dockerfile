FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirement.txt .
RUN pip install --upgrade pip && \
    pip install -r requirement.txt && \
    pip install uwsgi

# Copy the application files
COPY . .

# Expose the app port
EXPOSE 5000

# Run uWSGI with minimal configuration
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--module", "app:app"]
