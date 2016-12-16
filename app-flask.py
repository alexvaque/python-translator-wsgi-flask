#!/usr/bin/env python
# Alex Vaque TEST 

# I use Flaks framework
# Flask, like Django, Pyramid and others, are based on WSGI, an API standard for connecting Python Web frameworks to Web servers.
# We recommend to use Python Virtualenv or Docker 

#import Flask

from flask import Flask
from flask import abort, make_response
from flask import jsonify, request

# we can use 2 differnt API to detect the language - (1) detectlanguage or (2) langdetect
# The first detect better the languages but is not opensource
# (1) detectlanguage API disabled
import detectlanguage
# (2) langdetect API enabled
#from langdetect import detect

# Used for detectlangue - https://detectlanguage.com/ - 
detectlanguage.configuration.api_key = "2823c5789d302daa51787b57d5dd686a"

PORT=8080

app = Flask(__name__)

translations = [
    {
        'id': 1,
        'text': u'Me gusta leer libros',
        'language': u'es', 
    },
]

# Error management
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Extra: All the translations - historic translations - we can got an specific old translation using an ID 
@app.route('/<int:translation_id>', methods=['GET'])
def get_translation(translation_id):
    translation = [translation for translation in translations if translation['id'] == translation_id]
    if len(translation) == 0:
        abort(404)
    return jsonify({'translation': translation[0]})

# Extra: All the translations - historic translations 
@app.route('/', methods=['GET'])
def get_translations():
    return jsonify({'translations': translations})

# Exercise: web service that detects the language of an input string
@app.route('/', methods=['POST'])
def create_translation():
    if not request.json or not 'text' in request.json:
        abort(400)
    print request.json
    text = request.json['text']
    print text
    # Using 1rst API
    language2 = detectlanguage.simple_detect(text)
    # Using 2nd API
    #language2 = detect(text)

    print "Language Detected is - "+language2
    language = { 'language': request.json.get('language', language2),}

    translation = {
        'id': translations[-1]['id'] + 1,
        'text': request.json['text'],
        'language': request.json.get('language', language2),
    }
    translations.append(translation)
    return jsonify(language), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)


