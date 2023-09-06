
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class VocodeWebhook(generics.CreateAPIView):
    permission_classes = []  # Disable authentication

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        return Response(status=HTTP_200_OK, data={'message': "Webhook successful!"})