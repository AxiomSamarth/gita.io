import os
import utils
import uuid
from flask import Flask, jsonify, request, redirect, session

app = Flask(__name__)
app.secret_key = os.environ['secret_key']

@app.route('/', methods=['GET'])
def index():
    return {'message': 'Welcome to Gita API'}


@app.route('/login/', methods=['POST'])
def login():
    credentials = request.json
    if credentials['username'] and credentials['password']:
        result, status_code = utils.login(credentials)
        if status_code == 200:
            session['id'] = str(uuid.uuid4())
            return jsonify({'id': session['id']})
    return result, status_code


@app.route('/signup/', methods=['POST'])
def signup():
    credentails = request.get_json()
    if credentails['username'] and credentails['password']:
        result = utils.signup(credentails)
    return result


@app.route('/chapter/<chapter_number>/', methods=['GET'])
def get_chapter(chapter_number):
    session_id = request.headers.get('id', None)
    if session_id == session.get('id'):
        return utils.get_verse_from_db(chapter_number)
    return {'error_message': 'Session not found. Please login'}


@app.route('/chapter/<chapter_number>/verse/<verse_number>/', methods=['GET'])
def get_verse(chapter_number, verse_number):
    session_id = request.headers.get('id', None)
    if session_id == session.get('id'):
        return utils.get_verse_from_db(chapter_number, verse_number)
    return {'error_message': 'Session not found. Please login'}


@app.route('/logout/', methods=['POST'])
def logout():
    session_id = request.headers.get('id')
    if session_id == session.get('id'):
        del session['id']
        return {}, 200
    return {'error_message': 'Invalid Session'}, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
