# ...existing code...
from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded users dictionary (username: password)
users = {
    "alice": "password123",
    "bob": "qwerty",
    "charlie": "letmein"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # ...existing code...
    # POST method
    data = request.get_json() if request.is_json else request.form
    username = data.get('username')
    password = data.get('password')

    if username not in users:
        return jsonify({"message": "User does not exist."}), 200
    elif users[username] != password:
        return jsonify({"message": "Incorrect password."}), 200
    else:
        return jsonify({"message": f"Welcome, {username}!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
# ...existing code...
