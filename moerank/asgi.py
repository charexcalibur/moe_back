"""
ASGI config for moerank project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os
import django
from channels.routing import get_default_application
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from moerank.dota import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moerank.settings')
django.setup()

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # 【channels】（第6步）添加路由配置指向应用的路由模块
    'websocket': SessionMiddlewareStack(  # 使用Session中间件，可以请求中session的值
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})