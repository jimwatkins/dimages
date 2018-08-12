# Use an official Python runtime as a parent image
FROM python:latest

# server tools
RUN apt-get update && apt-get install -y \
        openssh-server \
        nano \
        vsftpd

RUN useradd -ms /bin/bash bridger 
RUN yes bridger | passwd bridger
RUN useradd -ms /bin/bash jim
RUN yes amanda | passwd jim


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
#CMD ["python", "app.py"]