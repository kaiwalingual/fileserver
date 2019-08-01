from flask import Flask, request, send_file
from datetime import datetime
from pathlib import Path
from PIL import Image
from io import BytesIO

base_dir = Path("pics")

app = Flask(__name__)


@app.route("/list", methods=["GET"])
def list_files():
    return ",".join(sorted([f.name for f in base_dir.iterdir() if f.is_file()]))


@app.route("/", methods=["POST"])
@app.route("/<name>", methods=["GET"])
@app.route("/min/<minname>", methods=["GET"])
def index(name=None, minname=None):
    if request.method == "POST":
        base_dir.mkdir(exist_ok=True)
        f = request.files["file"]
        fname = datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
        f.save(base_dir / fname)

        return fname
    if minname is not None:
        name = minname

    if name is None:
        return "specify a name at /<name>.jpg"

    path = base_dir / name
    if path.exists():
        if minname is not None:
            im = Image.open(base_dir / name)
            im.thumbnail((240, 240))
            im_io = BytesIO()
            im.save(im_io, "JPEG")
            im_io.seek(0)
            return send_file(im_io, mimetype="image/jpeg")
        return send_file(path, mimetype="image/jpeg")
    else:
        return "NO", 404


app.run(host="127.0.0.1", port="5000")
