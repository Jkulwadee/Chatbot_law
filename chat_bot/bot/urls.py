# bot.urls.py

from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView
    )

app_name ='bot_webhooks'
urlpatterns = [
    re_path(r'^490f6bacc8ef74ef4a570da029ec5b98053a6a51949f702ec12363eddc0f/$', FacebookWebhookView.as_view(), name='webhook'),
]