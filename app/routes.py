from flask import render_template
from turing_contract.codenames_info import codename_list
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote')
def vote():
    codename_s = codename_list()
    return render_template('vote.html',all_lines = codename_s)

@app.route('/top')
def top_stakers():
    codename_s = codename_list()
    return render_template('top_stakers.html',all_lines = codename_s)

@app.route('/teacher')
def teacher():
    return render_template('teacher_zone.html')