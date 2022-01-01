from moerank.settings import LOGGING
from channels.generic.websocket import JsonWebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
from django.core.cache import caches
import logging
logger = logging.getLogger('daphne')

class AsyncConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.match_id = self.scope['url_route']['kwargs']['match_id']
        # await cache.get('match_id')
        

        self.accept()
        # await self.send({
        #     "type": "websocket.accept",
        # })

    def receive_json(self, content=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        key = '{}_{}'.format(self.match_id, content['time'])

        win_rate = caches['realtime'].get(key)
        print('win_rate: ', win_rate)
        logger.info('win_rate: {}'.format(win_rate))
        res = {
            'win_rate': win_rate
        }
        self.send_json(content=res)
        # Or, to send a binary frame:

    def disconnect(self, close_code):

        self.close()