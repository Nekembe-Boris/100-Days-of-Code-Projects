from flask import Flask, render_template
import requests


app = Flask(__name__)


endpoint_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=endpoint_url)
data = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=data)

@app.route('/blog/<int:pid>')
def get_post(pid):
    return render_template("post.html", uid=pid, posts=data)


if __name__ == "__main__":
    app.run(debug=True)
