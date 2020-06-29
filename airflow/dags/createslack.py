import requests
import json
SLACK_TOKEN = 'xoxp-872305152423-858981884739-1194141524086-62b15ef1e64d58023d4c20153b5892ed'
def channel(channel):
    return requests.post('https://api.slack.com/methods/conversations.create', {
        'token': SLACK_TOKEN,
        'channel': channel,
        'is_private': False,
    }).json()
channel('anitha_airflow')
