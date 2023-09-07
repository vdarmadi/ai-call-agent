import logging

from django.conf import settings
from twilio.rest import Client

logger = logging.getLogger('django')


def send_confirmation(to_number: str, body: str):
    logger.info(f"Number: {to_number} Body: {body}")
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    if to_number and "+" not in to_number:
        to_number = "+" + to_number
    client.messages.create(
        from_=settings.TWILIO_FROM_NUMBER,
        body=body,
        to=to_number
    )
