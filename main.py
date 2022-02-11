from wsgiref.simple_server import make_server
from ListeVoitureService import wsgi_application
import os

port = int(os.environ.get('PORT', 8000))
server = make_server('0.0.0.0', port, wsgi_application)
server.serve_forever()