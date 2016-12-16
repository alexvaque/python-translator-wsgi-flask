#!/usr/bin/env python
# Alex Vaque TEST 

# we can use 2 differnt API to detect the language - (1) detectlanguage or (2) langdetect
# The first detect better the languages but is not opensource
# (1) detectlanguage API disabled
import detectlanguage
# (2) langdetect API enabled
#from langdetect import detect
import json
import webob
import wsgiservice
from wsgiservice import Resource, get_app, mount, validate, expires


# Used for detectlangue - https://detectlanguage.com/ - 
detectlanguage.configuration.api_key = "2823c5789d302daa51787b57d5dd686a"

@mount('/text={text}')
class IsTheLanguage(Resource):
    def POST(self, text):
      print text
      # Using 1rst API
      language2 = detectlanguage.simple_detect(text)
      # Using 2nd API
      #language2 = detect(text)
      print "Language Detected is - "+language2
      return {'language': language2}

# app is a WSGI app.
app = get_app(globals())
 
# Serve this service on port 8000
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print "Running on port 8000. POST it the http://localhost:8000/text=Hello+world"
    make_server('', 8000, app).serve_forever()

