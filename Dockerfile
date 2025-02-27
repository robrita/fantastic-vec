# Use the official Python image from the Docker Hub
FROM python:3.12.7-slim

# Set environment variable for the port
ENV PORT=8000

# Expose the port that the application will run on
EXPOSE 8000

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the Streamlit application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]