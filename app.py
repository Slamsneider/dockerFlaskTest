from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Simple in-memory data store
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Learn Docker", "completed": False}
]

# HTML template for the home page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Docker App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
        }
        .endpoint {
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        .method {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 3px;
            font-weight: bold;
            margin-right: 10px;
        }
        .get { background: #61affe; color: white; }
        .post { background: #49cc90; color: white; }
        .put { background: #fca130; color: white; }
        .delete { background: #f93e3e; color: white; }
    </style>
</head>
<body>
    <h1>🐳 Flask + Docker Application</h1>
    <p>Welcome to your Flask application running in Docker!</p>
    
    <h2>Available Endpoints:</h2>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/</code> - This home page
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/hello</code> - Simple hello world JSON response
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/tasks</code> - Get all tasks
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/tasks/&lt;id&gt;</code> - Get a specific task
    </div>
    
    <div class="endpoint">
        <span class="method post">POST</span>
        <code>/api/tasks</code> - Create a new task (JSON body: {"title": "Task name"})
    </div>
    
    <div class="endpoint">
        <span class="method put">PUT</span>
        <code>/api/tasks/&lt;id&gt;</code> - Update a task (JSON body: {"completed": true/false})
    </div>
    
    <div class="endpoint">
        <span class="method delete">DELETE</span>
        <code>/api/tasks/&lt;id&gt;</code> - Delete a task
    </div>
    
    <div class="endpoint">
        <span class="method get">GET</span>
        <code>/api/info</code> - Get server information
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page with API documentation"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/hello')
def hello():
    """Simple hello world endpoint"""
    return jsonify({
        "message": "Hello from Flask in Docker!",
        "status": "success"
    })

@app.route('/api/info')
def info():
    """Get server information"""
    return jsonify({
        "app": "Flask Docker Demo",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "Home page",
            "GET /api/hello": "Hello world",
            "GET /api/tasks": "List all tasks",
            "GET /api/tasks/<id>": "Get specific task",
            "POST /api/tasks": "Create task",
            "PUT /api/tasks/<id>": "Update task",
            "DELETE /api/tasks/<id>": "Delete task",
            "GET /api/info": "Server info"
        }
    })

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(tasks)

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": tasks[-1]['id'] + 1 if tasks else 1,
        "title": request.json['title'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    if request.json:
        if 'title' in request.json:
            task['title'] = request.json['title']
        if 'completed' in request.json:
            task['completed'] = request.json['completed']
    
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) so it's accessible from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
