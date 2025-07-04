# Vulnerable Flask Login Demo

This project is a deliberately insecure Flask web application designed to demonstrate username enumeration and other common authentication flaws. **It is for educational and ethical hacking demonstration purposes only.**

## Features
- Hardcoded user credentials (no password hashing)
- Username enumeration via distinct error messages
- No account lockout or brute-force protection
- Simple HTML login form and JSON API

## 🚨 Warning
**This application is intentionally vulnerable. Do NOT deploy it in production or expose it to the public internet.**

## Getting Started (Docker)

1. Build the Docker image:
   ```sh
   docker build -t vuln-login .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 vuln-login
   ```
3. Visit [http://localhost:5000/login](http://localhost:5000/login) in your browser.

## License
MIT

