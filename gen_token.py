# Generate a 2 random hex string for your webhook endpoint and the VERIFY_TOKEN
# You only need to create these 1 time; you can always change them later but
# you don't need to generate them constantly

import os, binascii
webhook_endpoint = (binascii.b2a_hex(os.urandom(30))).decode("utf-8")
print(webhook_endpoint)

VERIFY_TOKEN = (binascii.b2a_hex(os.urandom(25))).decode("utf-8") # put this value in bot.views.py
print(VERIFY_TOKEN)

# 490f6bacc8ef74ef4a570da029ec5b98053a6a51949f702ec12363eddc0f
# d7b54d1f820f595152c9e656913b06fbcb26572d703e7f4e76