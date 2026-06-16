import os
from flask import Flask, send_from_directory

# Point Flask to your React build folder
app = Flask(__name__, static_folder="../qr-validator/dist", static_url_path="")

# Catch-all route: serve index.html for any path
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    file_path = os.path.join(app.static_folder, path)

    # If the requested file exists (like JS/CSS), serve it
    if os.path.isfile(file_path):
        return send_from_directory(app.static_folder, path)

    # Otherwise, always serve index.html
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
