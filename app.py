from flask import Flask, jsonify, render_template

# Create the Flask app
app = Flask(__name__)

# Shared sample data used by both views
USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# Define a simple route
@app.route('/')
def home():
    return render_template('index.html', message="Welcome to our Flask app!", users=USERS)

# Define an API endpoint that returns some data
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(USERS)

# Health check endpoint (important for Azure)
@app.route('/health')
def health():
    return jsonify({"status": "Healthy"}), 200

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
