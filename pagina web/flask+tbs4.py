from crypt import methods
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    teacher_name = request.args.get('teacher_name')
    render_template('index.html', teacher_name=teacher_name)
