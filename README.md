# Best Cars Dealership - Full Stack Capstone Project

A full-stack web application for a national car dealership that allows customers to search dealerships by state and read/write reviews.

## Tech Stack
- **Frontend**: React, Bootstrap
- **Backend**: Django (Python), Node.js + Express
- **Databases**: SQLite (Django), MongoDB (dealers/reviews)
- **Microservices**: Flask (Sentiment Analysis)
- **DevOps**: Docker, Kubernetes, GitHub Actions

## Features
- Browse dealerships by state
- View dealer reviews with sentiment analysis
- User registration, login, and logout
- Authenticated users can post reviews
- Admin panel for managing car makes and models

## Architecture
- Django app serves as the main backend and proxy
- Node.js/MongoDB microservice handles dealers and reviews
- Flask microservice performs sentiment analysis
- React frontend for dynamic pages

## Setup

### Prerequisites
- Python 3.9+
- Node.js 18+
- Docker & Docker Compose

### Run locally
```bash
# Install Python dependencies
pip install -r server/requirements.txt

# Start MongoDB + Node.js backend
cd server/database
docker-compose up --build -d

# Start sentiment analyzer
cd server/djangoapp/microservices
docker build -t sentiment-analyzer .
docker run -d -p 5050:5000 sentiment-analyzer

# Start Django
cd server
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
