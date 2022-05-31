#https://getbootstrap.com/docs/4.3/getting-started/introduction/
#"pip install flask"
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Avaleht")
def home2():
    return render_template("index.html")

@app.route('/galerii')
def galerii():
    return render_template('galerii.html')

@app.route("/quiz-mäng")
def Quiz_game():
    return render_template("quiz.html")

@app.route("/video")
def video():
    return render_template("video.html")

@app.route('/kontakt')
def kaart():
    return render_template('kontakt.html')


@app.route('/kasutatud-materjal')
def materjal():
    return render_template('Kasutatud-materjal.html')

if __name__ == "__main__":
    app.run(debug=True)

