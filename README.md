# Student Course API

A simple REST API developed using Python Flask.

## Features
- Health check endpoint
- Display all courses
- Display one course by ID
- JSON responses
- CORS enabled

## Installation

pip install -r requirements.txt

## Run the application

python app.py

## API Endpoints

GET /
GET /api/health
GET /api/courses
GET /api/courses/1

## Deployment

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

