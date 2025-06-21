# Use the official Python image as a base
FROM python:3.13-slim

# Set work directory inside the container
WORKDIR /app

# Copy only the server directory into the image
COPY server/ ./server/

COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Set the default command to run your FastAPI app with uvicorn
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]