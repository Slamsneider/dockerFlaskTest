# Flask Docker Application

A simple Flask HTTP server running in Docker with a RESTful API for task management.

## Quick Start

### 1. Build the Docker Image
```bash
docker build -t flask-app .
```

### 2. Run the Container
```bash
docker run -d -p 5000:5000 --name my-flask-app flask-app
```

### 3. Access the Application
Open your browser and go to: **http://localhost:5000**

## Available URLs

- **http://localhost:5000** - Home page with API documentation
- **http://localhost:5000/api/hello** - Simple hello world endpoint
- **http://localhost:5000/api/tasks** - View all tasks
- **http://localhost:5000/api/info** - Server information

## API Endpoints

### GET /api/tasks
Get all tasks
```bash
curl http://localhost:5000/api/tasks
```

### POST /api/tasks
Create a new task
```bash
curl -X POST http://localhost:5000/api/tasks -H "Content-Type: application/json" -d "{\"title\":\"My new task\"}"
```

### PUT /api/tasks/<id>
Update a task
```bash
curl -X PUT http://localhost:5000/api/tasks/1 -H "Content-Type: application/json" -d "{\"completed\":true}"
```

### DELETE /api/tasks/<id>
Delete a task
```bash
curl -X DELETE http://localhost:5000/api/tasks/1
```

## Docker Commands

### View running containers
```bash
docker ps
```

### View logs
```bash
docker logs my-flask-app
```

### Stop the container
```bash
docker stop my-flask-app
```

### Start the container
```bash
docker start my-flask-app
```

### Remove the container
```bash
docker rm my-flask-app
```

### Remove the image
```bash
docker rmi flask-app
```

## Project Structure
```
dockerFlaskTest/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── .dockerignore      # Files to exclude from Docker
└── README.md          # This file
```
