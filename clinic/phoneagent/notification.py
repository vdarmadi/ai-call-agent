from django.conf import settings
from twilio.rest import Client


def send_confirmation(to_number: str, body: str):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    if to_number and "+" not in to_number:
        to_number += "+"
    message = client.messages.create(
        from_=settings.TWILIO_FROM_NUMBER,
        body=body,
        to=to_number
    )

    print(message.sid)
