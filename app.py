from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/aboutUs')
def aboutUs():
    return 'this is about us page'

@app.route('/contactus', methods=['POST'])
def contactUs():
    return 'this is contact us page'

if __name__ == '__main__':
    # Use WSGI server (such as gevent) to run Flask app in the background
    http_server = WSGIServer(('0.0.0.0', 3000), app)
    http_server.serve_forever()
