from flask import Flask, render_template, url_for

# 이 파일의 reference
application = app = Flask(__name__)

# set up route
@app.route('/')
def index():
    return render_template('index.html')

# piano 
@app.route("/piano")
def piano():
    return render_template('piano.html')

# game
@app.route("/game")
def game():
    return render_template('game.html')

# pets
@app.route("/pets")
def pets():
    return render_template('pets.html')

if __name__ == "__main__":
    app.run(debug=True)

 