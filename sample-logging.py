from flask import Flask, request
from sap.cf_logging import flask_logging
import os, logging

app = Flask(__name__)

#Iitialize logging
flask_logging.init(app, logging.INFO)

cf_port = os.getenv('PORT')

# Only get method by default
@app.route('/')
def hello():
    logger = logging.getLogger('my.logger')
    logger.info(request)
    print(request)
    return 'Hello World'

if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
