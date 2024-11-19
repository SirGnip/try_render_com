import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<p>Hello, World out there!</p>
<a href="/name/foo">Link to person: foo</a>
<p>
<a href="/name/bar">Link to person: bar</a>
<p>
<a href="/debug">Debug</a>
"""

@app.route("/name/<user>")
def name_route(user):
    return f"<h1>Hello to {user}</h1>"

@app.route("/debug")
def debug():
    return f"<h1>RENDER_SERVICE_NAME = {os.getenv('RENDER_SERVICE_NAME')}</h1>"

