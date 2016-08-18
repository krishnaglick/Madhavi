from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/videos')
def videos():
    return render_template("videos.html")


@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")


@app.route('/photos')
def photos():
    return render_template("photos.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
