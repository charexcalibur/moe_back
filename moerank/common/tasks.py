from celery import shared_task
import requests
import json


@shared_task
def notice(content):
    print('content: ', content)
    with open('/home/moeback/moerank/common/key.json', 'r') as f:
        data = json.load(f)

    key = data['server_key']
    url = 'https://sc.ftqq.com/{}.send'.format(key)
    payload = {
        'text': content['text'],
        'desp': content['desp']
    }
    requests.get(url, params=payload)