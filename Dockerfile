FROM python:3.9-slim
# FROM ubuntu:22.04

# RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
# RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker

# RUN DEBIAN_FRONTEND=noninteractive \
#     apt-get update \
#     && apt-get install -y python3 \
#     && rm -rf /var/lib/apt/lists/*

# RUN useradd -ms /bin/bash apprunner
# USER apprunner

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 80

# Run the FastAPI application using uvicorn server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
