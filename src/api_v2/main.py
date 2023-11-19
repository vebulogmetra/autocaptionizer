import os

from flask import Flask, abort, render_template, request
from werkzeug.utils import secure_filename

from src.conf import Config
from src.ml.v2 import get_caption

app = Flask(__name__, template_folder=Config.templates_path)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["ALLOWED_EXTENSIONS"] = Config.allowed_extensions
app.config["UPLOAD_PATH"] = Config.uploaded_images_path


def allowed_file(filename: str):
    _, ext = filename.lower().split(".")
    return ext in app.config["ALLOWED_EXTENSIONS"]


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_files():
    if "file" not in request.files:
        abort(403, "Forbidden")
    uploaded_file = request.files["file"]
    if uploaded_file.filename == "":
        abort(400, "Bad Request")
    if allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(app.config["UPLOAD_PATH"], filename)
        uploaded_file.save(filepath)
        caption = get_caption(image_path=filepath, transl=Config.translate_captions)
        return render_template(
            "upload_success.html", caption=caption, uploaded_image=filepath
        )
    else:
        abort(400, "Bad Request")


if __name__ == "__main__":
    app.run(debug=True)
