from flask import Flask, request
from sys import argv
import pacmd_handler
import json
import os
app = Flask(__name__)

def file_get_contents(fpath, binary=False):
    if binary:
        mode = 'rb'
    else:
        mode = 'r'
    with open(fpath, mode) as f:
        return f.read()

@app.route('/pa_data.json')
def get_pa_data():
    data = {}
    data.update(pacmd_handler.get_sinks())
    data.update(pacmd_handler.get_sink_inputs())
    return json.dumps(data)

@app.route('/pa_control', methods=['POST'])
def pa_control():
    data = request.get_json()
    method = data.get('method', None)
    # if method:
        

@app.route("/")
def hello():
    return file_get_contents('index.htm')

if __name__ == '__main__':
    host = '0.0.0.0'
    if 'debug' in argv:
        app.debug = True
    if 'localhost' in argv:
        host = 'localhost'
    app.run(host=host, port=5000, threaded=True)
