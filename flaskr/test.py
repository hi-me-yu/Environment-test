from flaskr import app
from flask import render_template #HTMLのデータを読み込んでPythonのデータに埋め込んで表示させる ※jinja2を使ってる

@app.route("/")
def index():
    return render_template("index.html")