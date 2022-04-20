from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Party!</h1>'

if __name__ == '__main__':
    app.run()