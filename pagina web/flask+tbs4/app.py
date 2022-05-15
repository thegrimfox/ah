from flask import Flask
from flask import request
from flask import render_template
import bs4
import requests

app = Flask(__name__)


def get_horarios():
    return requests.get("http://horarios.ulagos.cl/1er%20semestre%202022_teachers_days_horizontal.html").text


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    teacher_name = request.form['teacher_name']
    html_text = get_horarios()
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    return render_template('search.html', teacher_name=teacher_name)
