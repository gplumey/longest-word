from flask import Flask, render_template, request, session
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)
SESSION_TYPE='filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid, score=get_score())


@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if is_valid:
        add_score(len(word))
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word, score=get_score())

def get_score():
    score = session.get("score")
    if not score:
        score = 0
    return score

def add_score(points):
    curr = get_score()
    session["score"] = curr + points
