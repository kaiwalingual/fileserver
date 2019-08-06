from flask import Flask, request, send_file
from datetime import datetime
from pathlib import Path
from PIL import Image
from io import BytesIO
import subprocess
import os

from tokens import GDRIVE_PARENT_DIR

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
        with open(base_dir / fname, "wb") as out:
            f.save(out)

        proc = subprocess.run(["gdrive", "upload", "-p", GDRIVE_PARENT_DIR, base_dir / fname],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        driveid = proc.stdout.decode("utf8").split("\n")[1].split(" ")[1]

        with open(base_dir / (fname + ".txt"), "w") as f:
            f.write(driveid)

        os.remove(base_dir / fname)

        return fname
    if minname is not None:
        name = minname

    if name is None:
        return "specify a name at /<name>.jpg"

    path = base_dir / (name + ".txt")
    if path.exists():
        gdriveid = ""
        with open(path) as f:
            gdriveid = f.readline()
        subprocess.run(["gdrive", "download", gdriveid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if minname is not None:
            im = Image.open(name)
            im = im.convert("RGB")
            im.thumbnail((240, 240))
            im_io = BytesIO()
            im.save(im_io, "JPEG")
            im_io.seek(0)
            os.remove(name)
            return send_file(im_io, mimetype="image/jpeg")

        im = Image.open(name)
        im = im.convert("RGB")
        im_io = BytesIO()
        im.save(im_io, "JPEG")
        im_io.seek(0)
        os.remove(name)
        return send_file(im_io, mimetype="image/jpeg")
    else:
        return "NO", 404


app.run(host="127.0.0.1", port="5000")
