import logging

from django.conf import settings
from twilio.rest import Client

logger = logging.getLogger('django')


def send_confirmation(to_number: str, body: str):
    """
        Sends a confirmation SMS using Twilio to the specified phone number.

        Args:
            to_number (str): The recipient's phone number in E.164 format (e.g., +1234567890).
            body (str): The message text to send in the SMS.

        Returns:
            None

        Example:
            send_confirmation("+1234567890", "Your appointment is confirmed for tomorrow at 2 PM.")
    """
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
