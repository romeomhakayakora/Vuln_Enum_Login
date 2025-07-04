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
        # Return a styled and centered HTML login form
        return '''
        <html>
        <head>
            <title>Login</title>
            <style>
                body {
                    background: #f8f9fa;
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .login-container {
                    background: #fff;
                    padding: 2rem 2.5rem;
                    border-radius: 12px;
                    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                .login-container h2 {
                    margin-bottom: 1.5rem;
                    color: #343a40;
                }
                .login-container input {
                    width: 220px;
                    padding: 0.5rem 0.75rem;
                    margin-bottom: 1rem;
                    border: 1px solid #ced4da;
                    border-radius: 6px;
                    font-size: 1rem;
                }
                .login-container button {
                    width: 100%;
                    padding: 0.5rem 0;
                    background: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 6px;
                    font-size: 1rem;
                    cursor: pointer;
                    transition: background 0.2s;
                }
                .login-container button:hover {
                    background: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Login</h2>
                <form method="post" action="/login" id="loginForm">
                    <input type="text" name="username" placeholder="Username" required><br>
                    <input type="password" name="password" placeholder="Password" required><br>
                    <button type="submit">Login</button>
                </form>
                <div id="login-message" style="margin-top:1rem;color:#d9534f;"></div>
            </div>
            <script>
            document.getElementById('loginForm').onsubmit = async function(e) {
                e.preventDefault();
                const form = e.target;
                const username = form.username.value;
                const password = form.password.value;
                const res = await fetch('/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                });
                const data = await res.json();
                document.getElementById('login-message').textContent = data.message;
            };
            </script>
        </body>
        </html>
        '''
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
