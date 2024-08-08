from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/421ecf314896a263150c").json()

def send(*args):
    MY_EMAIL = "aminaousmanu@gmail.com"
    PASSWORD = "PASSWORD"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg=f"Subject:Happy Birthday\n\nName:{args[0]}\nEmail:{args[1]}\nTel:{args[2]}\nMessage:{args[3]}"
        )

app = Flask(__name__)



@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", data=True)
    user_name = request.form["username"]
    email = request.form["user_email"]
    tel = request.form["phone"]
    message = request.form["message"]
    send((user_name, email, tel, message))

    return render_template("contact.html", data=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
