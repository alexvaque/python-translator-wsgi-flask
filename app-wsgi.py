#!/usr/bin/env python
# Alex Vaque TEST 

# I use WSGI but I prefer to use frameworks like Flask for Sysadmins or Django for big projects 
# boths frameworks are based on WSGI, an API standard for connecting Python Web frameworks to Web servers.


import urlparse
import wsgiref.simple_server

try:
    import json
except:
    import simplejson as json

# we can use 2 differnt API to detect the language - (1) detectlanguage or (2) langdetect
# The first detect better the languages but is not opensource
# (1) detectlanguage API disabled
import detectlanguage
# (2) langdetect API enabled
#from langdetect import detect

# Used for detectlangue - https://detectlanguage.com/ - 
detectlanguage.configuration.api_key = "2823c5789d302daa51787b57d5dd686a"

translations = [
    {
        'id': 1,
        'text': u'Me gusta leer libros',
        'language': u'es',
    },
]



def servidor(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    if environ["REQUEST_METHOD"] == "GET":
	return json.dumps([False, translations])

    elif environ["REQUEST_METHOD"] == "POST":
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0

        request_body = environ['wsgi.input'].read(request_body_size)
        data = json.loads(request_body)
        text = data['text']

	# Using 1rst API
	language2 = detectlanguage.simple_detect(text)
	# Using 2nd API
	#language2 = detect(text)

	print "Language Detected is - "+language2

        try:
            return ["{\"language\": \"" + str(language2)+"\"}"]
        except:
            return ["error "]

    else:
        return json.dumps([False, { 'msg': "Rest api error)" }])


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, servidor)
    srv.serve_forever()

