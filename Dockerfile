
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Prevent Python from writing .pyc files and enable stdout/stderr unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# Install system build dependencies required by some Python packages
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   build-essential \
	   gcc \
	   libssl-dev \
	   libffi-dev \
	   cargo \
	   git \
	&& rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requierements.txt /app/requierements.txt
RUN pip install --upgrade pip setuptools wheel \
	&& pip install --no-cache-dir -r /app/requierements.txt

# Copy the project into the container. Keep the repo folder name so
# package imports like `chatbot_rag.main` work (main uses relative imports).
COPY . /app/chatbot_rag

# Ensure Python can import the package by adding /app to PYTHONPATH
ENV PYTHONPATH=/app

# Expose port used by Uvicorn
EXPOSE 8000

# Default command to run the FastAPI app using Uvicorn
#CMD ["uvicorn", "chatbot_rag.main:app", "--host", "0.0.0.0", "--port", "8000"]

