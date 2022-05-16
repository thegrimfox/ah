from flask import Flask
from flask import request
from flask import render_template
import bs4
import requests

app = Flask(__name__)


def get_rut():
    return requests.get("https://www.nombrerutyfirma.com/rut?term=19.963.750-9").text


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    rut_name = request.form['rut_name']
    html_text = get_rut()
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    return render_template('search.html', rut_name=rut_name)
