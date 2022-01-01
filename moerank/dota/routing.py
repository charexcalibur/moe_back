from django.conf.urls import url
from moerank.dota.views import realtime
from django.urls import path

websocket_urlpatterns = [
    path('ws/msg/<match_id>/', realtime.AsyncConsumer.as_asgi()),
]
