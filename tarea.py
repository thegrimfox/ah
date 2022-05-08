from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/user/<name>')
def user(name='joako'):
    return render_template('tarea.html')
