from flask import Flask,  render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/tulokset')
def tulokset():
    return render_template('tulokset.html')