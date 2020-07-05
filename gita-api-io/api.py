import os
import requests
import json
from flask import Flask, render_template, request, redirect, flash, jsonify, session, url_for

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
gita_io = 'http://localhost:8080/'
requests_ = requests.Session()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if session.get('id'):
            return render_template('index.html', id=session['id'], verse=None)
        return render_template('login.html')
    credentials = request.form
    response = requests_.post(url=gita_io+'login/', json=credentials)
    response_body = json.loads(response.text)
    if response.status_code == 200:
        id = response_body.get('id')
        session['id'] = id
        return render_template('index.html', id=id)
    flash(response_body['error_message'])
    return redirect(url_for('login'))


@app.route('/signup/', methods=['GET'])
def signup():
    return render_template('signup.html')


@app.route('/verse/', methods=['POST'])
def verse():
    chapter_number = request.form.get('chapter_number')
    verse_number = request.form.get('verse_number')
    if verse_number is None:
        verse_number = 1
    headers = {'id': request.form.get('id')}
    response = requests_.get(url=gita_io+'chapter/{}/verse/{}/'.format(chapter_number, verse_number), headers=headers)
    response_body = json.loads(response.text)
    if response.status_code == 200:
        return render_template('index.html', id=headers['id'] verse=json.loads(response.text))
    flash(response_body['error_message'])
    return render_template('index.html', id=headers['id'], verse=None)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    del session['id']
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)