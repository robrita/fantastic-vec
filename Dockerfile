# Use the official Python image from the Docker Hub
FROM python:3.12.7-slim

# Set environment variable for the port
ENV PORT=8501

# Expose the port that the application will run on
EXPOSE 8501

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]