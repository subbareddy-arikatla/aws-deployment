# # Use the official Python image
# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set the working directory in the container
# WORKDIR /myapp

# # Install dependencies
# COPY requirements.txt /myapp/
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy the rest of the code
# COPY . /app

FROM python:3.12-slim

# Set working directory
WORKDIR /myapp

# Copy requirements
COPY requirements.txt /myapp/

# Install dependencies
RUN pip install --upgrade pip && pip install -r /myapp/requirements.txt

# Copy project
COPY . /myapp/

# Expose port
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
