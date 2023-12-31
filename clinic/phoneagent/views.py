from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from vocode.client import Vocode

from clinic.phoneagent.constants import EVENT_PHONE_CALL_ENDED
from clinic.phoneagent.notification import send_confirmation
from clinic.phoneagent.parser import parse_appointment_detail


class VocodeWebhook(generics.CreateAPIView):
    permission_classes = []  # Disable authentication

    def post(self, request, *args, **kwargs):
        try:
            vocode_client = Vocode(
                token=settings.VOCODE_TOKEN
            )
            webhook_type = request.data['type']

            if EVENT_PHONE_CALL_ENDED == webhook_type:
                # Get call detail.
                call_id = request.data['call_id']
                call = vocode_client.calls.get_call(id=call_id)
                conversation = call.transcript

                # Extract appointment detail.
                doctor_name, appointment_date_time = parse_appointment_detail(conversation)

                if doctor_name and appointment_date_time:
                    # Send confirmation via text message.
                    text_message = f"You are confirmed with Doctor {doctor_name} on {appointment_date_time}."
                    to_number = call.from_number
                    if to_number:
                        send_confirmation(to_number, text_message)
        except Exception:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR, data={'message': "Internal Server Error."})

        return Response(status=HTTP_200_OK, data={'message': "Webhook successful."})
