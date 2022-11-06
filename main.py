from flask import Flask
from utils import *


candidates = load_candidates('candidates.json')
app = Flask(__name__)


@app.route('/')
def page_main():
    """главная страница, выводим всех кандидатов"""
    return get_all(candidates)


@app.route("/candidate/<int:pk>/")
def page_candidates(pk):
    """необходимо вывести номер кандидата"""
    return get_by_pk(pk, candidates)


@app.route("/skills/<skill_name>")
def page_skill(skill_name):
    """вывод навыков кандидата"""
    return get_by_skill(skill_name, candidates)

app.run(host='127.0.0.1', port=7000)