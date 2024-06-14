# wechat/urls.py
from django.urls import path
# from .views import send_wechat_message

urlpatterns = [
    path('send/<int:message_id>/', send_wechat_message, name='send_wechat_message'),
]