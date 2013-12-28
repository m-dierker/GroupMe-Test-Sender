#!/usr/bin/env python
""" A general purpose tester to send test messages to a user's groups """
""" This is as a convenience for Matthew to test from Alfred without loading the GroupMe app """
import json
from flask import Flask
from uuid import uuid4
import requests
import urllib

app = Flask(__name__)
config = None

@app.route("/send/<group_id_index>/<msg>")
def send_message(group_id_index, msg):
    group_id = config['groupIds'][int(group_id_index)]['id']
    msg = urllib.unquote(msg).decode('utf8')
    message_data = {
        'message': {
            'source_guid': str(uuid4()),
            'text': msg
        }
    }
    url = "https://api.groupme.com/v3/groups/%s/messages?token=%s" % (group_id, config['accessToken'])
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(message_data), headers=headers)
    return r.text

def get_config():
    with open('config.json') as json_data:
        data = json.load(json_data)
    return data

def start():
    global config
    config = get_config()
    app.run(debug=True, host='0.0.0.0', port=config['port'])

start()