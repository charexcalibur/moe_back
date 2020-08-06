'''
Description: init_data
Author: hayato
Date: 2020-08-05 21:19:17
LastEditors: hayato
LastEditTime: 2020-08-06 23:04:37
'''
import os
import sys
from qiniu import Auth, BucketManager
import django
from django.conf import settings
import json
sys.path.append('/Users/hayato/mywork/moerank')
print('sys.path: ', sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'moerank.settings'

django.setup()

from moerank.common.models import CoserInfo, CoserNoPic

with open('moerank/qiniu.json', 'r') as f:
    data = json.load(f)

access_key = data['access_key']
secret_key = data['secret_key']

q = Auth(access_key, secret_key)
bucket = BucketManager(q)

bucket_name = 'mikumoe'

prefix = 'yami'

limit = 1000

delimiter = None

marker = None

result_list = []

count = 0

URL = 'https://moe.axis-studio.org/'

def get_item(bucket_name, prefix, marker, limit, delimiter, count, result_list):
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    url_list = [URL+item['key'] for item in ret.get('items')]
    result_list = result_list + url_list

    count = count + 1
    print(count)
    if eof:
        print('result_list: ', result_list)
        return result_list
    else:
        marker = ret['marker']
        return get_item(bucket_name, prefix, marker, limit, delimiter, count, result_list)

result_list = get_item(bucket_name, prefix, marker, limit, delimiter, count, result_list)

print('ret: ', result_list)
coser_query_set = CoserInfo.objects.get(name_en=prefix)

for item in result_list:

    save_data = {
        'coser': coser_query_set,
        'url': item
    }

    CoserNoPic.objects.create(**save_data)
