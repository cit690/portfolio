from flask import Flask, render_template, url_for
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', methods=['GET'])

@app.route('/debug/<thing>')
def debug_test(thing):
    return "100th letter: {}".format(thing[100])

if __name__ == '__main__':
    app.run()