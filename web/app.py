from flask import Flask, render_template, request
import os

from backend.checker import run_checker

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    report = None

    if request.method == "POST":
        file = request.files.get("zipfile")
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            report = run_checker(file_path)

    return render_template("index.html", report=report)


if __name__ == "__main__":
    app.run(debug=True)
