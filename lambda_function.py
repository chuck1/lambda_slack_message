import os
from slackclient import SlackClient

def post_message(sc, channel, text):
    res = sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=text,
            )
    print("post message. channel={} text={}".format(repr(channel), repr(text)));
    print(res)

def lambda_handler(event, context):

    slack_token = os.environ["SLACK_TOKEN"]
    
    sc = SlackClient(slack_token)
    
    for c in event['Commands']:
        if c['Type'] == 'PostMessage':
            post_message(sc, c['Data']['Channel'], c['Data']['Text'])

    return 'Hello from Lambda'

