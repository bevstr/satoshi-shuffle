FROM python:3.9-slim


# Install tini to handle zombie processes
RUN apt-get update && apt-get install -y tini

# Set tini as the init system
ENTRYPOINT ["/usr/bin/tini", "--"]

WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY webapp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose the port the app runs on
EXPOSE 5010

# Create volumes for persistent data
VOLUME ["/app/logs", "/app/config"]

# Command to run the application
CMD ["python", "webapp/blockclock_web.py"]