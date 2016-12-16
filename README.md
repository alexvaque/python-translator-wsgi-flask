# python-translator-wsgi-flask



# 1 - Launch WSGISERVICE APP 

 python app-wsgiservice.py


curl -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" -d "/text" "http://localhost:8000/text=Hello+world.+Hs+the+sun+risen+on+you+today%3F"


{"language": "en"}


curl -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" -d "/text" "http://localhost:8000/text=Vaig+neixer+a+un+poble+de+Tarragona%3F"

{"language": "ca"}

curl -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" -d "/text"  "http://localhost:8000/text=Pero+hace+casi+doce+años+que+estoy+en+Barcelona%3F"

{"language": "es"}



# 2 - Launch WSGI APP 

 python app-wsgi.py

$ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Je suis Francais"}' http://localhost:8080/
HTTP/1.0 200 OK
Date: Thu, 09 Jul 2015 19:54:40 GMT
Server: WSGIServer/0.1 Python/2.7.6
Content-Type: application/json
Content-Length: 18

{"language": "fr"}

$ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Yo soy español"}' http://localhost:8080/
HTTP/1.0 200 OK
Date: Thu, 09 Jul 2015 19:54:45 GMT
Server: WSGIServer/0.1 Python/2.7.6
Content-Type: application/json
Content-Length: 18

{"language": "es"}

$ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"I am English"}' http://localhost:8080/
HTTP/1.0 200 OK
Date: Thu, 09 Jul 2015 19:54:48 GMT
Server: WSGIServer/0.1 Python/2.7.6
Content-Type: application/json
Content-Length: 18

{"language": "en"}


# 3 - Launch Flask APP 

$python app-flask.py

$ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Je suis Francais"}' http://localhost:8080/
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/0.10.4 Python/2.7.6
Date: Thu, 09 Jul 2015 19:54:13 GMT

{
  "language": "fr"
}


$ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Yo soy español"}' http://localhost:8080/
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/0.10.4 Python/2.7.6
Date: Thu, 09 Jul 2015 19:54:21 GMT

{
  "language": "es"
}


$ curl -i -H "Content-Type: application/json" -X POST -d '{"text":"I am English"}' http://localhost:8080/
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/0.10.4 Python/2.7.6
Date: Thu, 09 Jul 2015 19:54:28 GMT

{
  "language": "en"
}




