from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
