from flask import Flask, render_template
from data import GAME, SCREENSHOTS, FEATURES

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        game=GAME,
        screenshots=SCREENSHOTS,
        features=FEATURES
    )

if __name__ == "__main__":
    app.run(debug=True)
