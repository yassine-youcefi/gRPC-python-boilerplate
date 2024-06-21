# Use the official Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 5000

# Run server.py when the container launches using watchdog
CMD ["watchmedo", "auto-restart", "--recursive", "--patterns=*.py", "python3", "server.py"]
