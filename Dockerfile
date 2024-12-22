FROM python:3.9-slim



# Install Python dependencies
RUN pip install --upgrade pip

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
CMD ["python3", "app.py", "--host=0.0.0.0"]
