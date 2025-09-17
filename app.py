# app.py
from flask import Flask, jsonify

# Create the Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to our Flask API!"})

# Define an API endpoint that returns some data
@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return jsonify(users)

# Health check endpoint (important for Azure)
@app.route('/health')
def health():
    return jsonify({"status": "Healthy"}), 200

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)