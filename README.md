# Django Capstone - Portfolio & Users

Welcome to the Django Capstone Project - My portfolio aswell as user authentication with the Django framework.

## Table of Contents
1. [Environment Setup](#environment-setup)
    - [Step 1: Clone the Repository](#step-1-clone-the-repsitory)
    - [Step 2: Create Virtual Environment](#step-3-create-virtual-environment)
    - [Step 3: Build the Docker Image](#step-4-pull-docker-image-from-dockerhub)
    - [Step 4: Find the Port](#step-5-build-the-docker-image)
    - [Step 5: Access the Application](#step-6-run-docker-container)

## Environment Setup

Clone the repository, setup your Python virtual environment then setup Docker to run Django website. Instructions below.

### Step 1: Clone the Repository

```bash
git clone Django-Capstone.git
```

### Step 2: Create Virtual Environment

```bash
python -m virtualenv venv
```

### Step 3: Pull Docker Image from DockerHub

```bash
docker pull bonganicacambile/capstone
```

### Step 4: Build the Docker Image

```bash
docker build -t bonganicacambile/capstone ./
```

### Step 5: Run Docker Container

```bash
docker run -p 8000:8000 bonganicacambile/capstone
```

### Step 6: Access the Website

[capstone-website](http://127.0.0.1:8000)

You should now be able to access the Django Web Application in your browser.

---
**Developed by Bongani Cacambile**