import os
from db import get_client
from flask import jsonify
from hashlib import md5

db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']

def login(credentials):
    try:
        client = get_client(db_host, db_port)
        database = client['gita-db']
        user_collection = database['users']
        credentials['password'] = md5(credentials['password'].encode()).hexdigest()
        user = user_collection.find_one(credentials)
        if user:
            return user, 200
        else:
            return {'error_message': 'Invalid credentials'}, 401
    except Exception:
        return {'error_message': 'Something went wrong while logging in'}, 500


def signup(credentials):
    try:
        client = get_client()
        database = client['gita-db']
        user_collection = database['users']
        if not user_collection.find_one({'username': credentials['username']}):
            credentials['password'] = md5(credentials['password'].encode()).hexdigest()
            user_collection.insert_one(credentials)
            return {}
        return {'error_message': 'User already exists. Please login'}, 400
    except Exception:
        return {'error_message': 'Something went wrong while signing up'}, 500


def get_verse_from_db(chapter_number=None, verse_number=None):
    try:
        client = get_client()
        database = client['gita-db']
        gita_collection = database['gita-verses']

        if chapter_number:
            query = dict()
            query['chapter'] = int(chapter_number)
            if verse_number:
                query['verse_number'] = int(verse_number)
                verse = gita_collection.find_one(query)
                client.close()
                if verse:
                    return jsonify(verse), 200
                else:
                    return {'error_message': 'Verse {} not found in '\
                        'chapter {}'.format(verse_number, chapter_number)}, 404
            verses = gita_collection.find(query)
            client.close()
            if verses:
                return jsonify(list(verses)), 200
            else:
                return {'error_message': 'Chapter {} ' \
                    'not found'.format(chapter_number)}, 404
        return {'error_message': 'Verse {} not found in chapter {}'.format(
            verse_number, chapter_number)}, 404
    except Exception:
        return {'error_message': 'Something went wrong!'}, 500
