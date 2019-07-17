from flask import Flask, request, send_file
from datetime import datetime
from pathlib import Path
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["POST"])
@app.route("/<name>", methods=["GET"])
@app.route("/<min>/<name>", methods=["GET"])
def index(name=None, min=None):
    if request.method == "POST":
        f = request.files["file"]
        fname = datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
        f.save(f"pics/{fname}")
        
        return fname

    if name is None:
        return "specify a name at /<name>.jpg"

    path = Path(f"pics/{name}")
    if path.exists():
        if min is not None:
            im = Image.open(f"pics/{name}")
            im.thumbnail((240,240))
            im_io = BytesIO()
            im.save(im_io,"JPEG")
            im_io.seek(0)
            return send_file(im_io, mimetype="image/jpeg")
        return send_file(path, mimetype="image/jpeg")
    else:
        return "NO", 404

app.run(host="127.0.0.1", port="5000")
