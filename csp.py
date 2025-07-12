from flask import Flask, request, current_app
from flask_csp import CSP

app = Flask(__name__)

# Define your Content Security Policy (CSP)
csp_policy = {
    "default-src": "'none'",
    "script-src": ["'self'", "'https://code.jquery.com'"],
    "style-src": ["'self'", "'https://fonts.googleapis.com'"],
    "font-src": ["'self'", "'https://fonts.gstatic.com'"],
}

# Create a CSP object and configure it
csp = CSP(app, policy=csp_policy)

@app.before_request
def before_request():
    # Set the Content-Security-Policy header on each request
    csp.apply()

if __name__ == "__main__":
    app.run(debug=True)
