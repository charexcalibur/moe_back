from celery import shared_task
import requests
import json
from moerank.fhc.models import QuotationsVote, Quotations
from moerank.fhc.serializers.quotations import QuotationsVoteSerializer
import time

@shared_task
def notice(content, **kwargs):
    print('content: ', content)
    with open('/home/moe_back/moerank/common/key.json', 'r') as f:
        data = json.load(f)

    key = data['server_key']
    url = 'https://sc.ftqq.com/{}.send'.format(key)
    payload = {
        'text': content['text'],
        'desp': content['desp']
    }
    requests.get(url, params=payload)

@shared_task
def vote(quotation_id):
    que_queryset = Quotations.objects.filter(id=quotation_id['quotation_id']).first()
    save_data = {
        'quotation': que_queryset,
    }
    q = QuotationsVote.objects.create(**save_data)
    seriazlier = QuotationsVoteSerializer(q)
    return seriazlier.data