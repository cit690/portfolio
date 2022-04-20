from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debug/<thing>')
def debug_test(thing):
    return "100th letter: {}".format(thing[100])

if __name__ == '__main__':
    app.run()