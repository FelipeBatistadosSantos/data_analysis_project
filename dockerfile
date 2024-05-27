# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory contents into the container at /usr/src/app
COPY . .

# Install the package in editable mode
RUN pip install --no-cache-dir -e .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "src/main.py"]
