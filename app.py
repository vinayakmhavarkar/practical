from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
