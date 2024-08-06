from flask import Flask, render_template
import requests

app = Flask(__name__)

url_endpoint = "https://api.npoint.io/421ecf314896a263150c"
response = requests.get(url=url_endpoint)
DATA = response.json()

@app.route('/')
def home():
    return render_template('index.html', posts=DATA)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/post/<int:uid>')
def post_page(uid):
    return render_template('post.html', posts=DATA, pid=uid)

if __name__ == '__main__':
    app.run(debug=True)
