from flask import Flask
from random import randint

app = Flask(__name__)
CHOSEN = randint(0, 9)
# print(CHOSEN)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<iframe src="https://giphy.com/embed/3NtY188QaxDdC" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'

@app.route("/<int:num>")
def guess(num):
    if num > CHOSEN:
        return '<h1 style ="color:blue">Too high, try again </h1>' \
        '<iframe src="https://giphy.com/embed/j0gQA2VD38NKc9rc8y" width="480" height="398" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    if num < CHOSEN:
        return '<h1 style ="color:red">Too Low, try again! </h1>' \
        '<iframe src="https://giphy.com/embed/pPwL8pCLs2kZq" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    return '<h1 style ="color:green">BooYah</h1>' \
        '<iframe src="https://giphy.com/embed/tIeCLkB8geYtW" width="480" height="379" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


if __name__ == "__main__":
    app.run(debug=True)
