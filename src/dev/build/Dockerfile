# Use an official Python runtime as a parent image
FROM python:3.10

RUN apt-get update && apt-get install -y build-essential

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV="development"

# Set working directory in the container
WORKDIR /app

# Copy requirements file first to leverage Docker cache
COPY ./src/dev/requirements.txt /app/

# Upgrade pip and install requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application
COPY . /app/

# Copy entrypoint script into the container root
COPY ./src/dev/build/entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Create a non-root user and group
RUN useradd --create-home admin
RUN chown -R admin /app

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]