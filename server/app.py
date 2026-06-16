import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../qr-validator/dist", static_url_path="")

# Serve static files from dist
@app.route('/<path:path>')
def static_proxy(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        # Always serve index.html for React Router routes
        return send_from_directory(app.static_folder, 'index.html')

# Root route
@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
