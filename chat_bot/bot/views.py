# bot.views.py
import json
from unittest import result
import requests, random, re
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .logic import LOGIC_RESPONSES

import random
from django.apps import apps
from . import word_utils

VERIFY_TOKEN = "d7b54d1f820f595152c9e656913b06fbcb26572d703e7f4e76"  # generated above

"""
FB_ENDPOINT & PAGE_ACCESS_TOKEN
Come from the next step.
"""
FB_ENDPOINT = "https://graph.facebook.com/v12.0/"
PAGE_ACCESS_TOKEN = "EAAeGA2LZAObIBAGOnBgxUIbwWoLR4m43rhkmkF9U1bZAps1ZCnIHlYhpdm5CWPlmQWtZALj9CwoN3ngtmIfqABAk6vofu4O42ktgxct2LRpRkEZBrfq8BWcxh7co0WdaD8rrgZA4Q85BXZCBiv0MduR9rJGC4sriiE1qZAZBeLMUIh3jZBQffd4zxl"


def parse_and_send_fb_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    # tokens = re.sub(r"[^a-zA-Z0-9\s]", " ", recevied_message).lower().split()
    print(recevied_message)
    classifier = apps.get_app_config("bot").classifier
    responses = apps.get_app_config("bot").responses

    tokens = recevied_message.lower()  # .split()
    msg = None
    feature = word_utils.get_features(tokens)
    result = classifier.prob_classify(feature)
    if result.prob(result.max()) < 0.5:
        msg = random.choice(responses["unknow-message"])

    msg = random.choice(responses[result.max()])

    if msg is not None:
        endpoint = f"{FB_ENDPOINT}/me/messages?access_token={PAGE_ACCESS_TOKEN}"
        response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": msg}})
        status = requests.post(
            endpoint, headers={"Content-Type": "application/json"}, data=response_msg
        )
        print(status.json())
        return status.json()
    return None


class FacebookWebhookView(View):
    @method_decorator(csrf_exempt)  # required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  # python3.6+ syntax

    """
    hub.mode
    hub.verify_token
    hub.challenge
    Are all from facebook. We'll discuss soon.
    """

    def get(self, request, *args, **kwargs):
        hub_mode = request.GET.get("hub.mode")
        hub_token = request.GET.get("hub.verify_token")
        hub_challenge = request.GET.get("hub.challenge")
        if hub_token != VERIFY_TOKEN:
            return HttpResponse("Error, invalid token", status_code=403)
        return HttpResponse(hub_challenge)

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Hello, World!")

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode("utf-8"))
        for entry in incoming_message["entry"]:
            for message in entry["messaging"]:
                if "message" in message:
                    fb_user_id = message["sender"]["id"]  # sweet!
                    fb_user_txt = message["message"].get("text")
                    if fb_user_txt:
                        parse_and_send_fb_message(fb_user_id, fb_user_txt)
        return HttpResponse("Success", status=200)
