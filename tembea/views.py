from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Services, Gallery

from api.serializers import ServicesSerializer
from api.serializers import GallerySerializer
# Create your views here.
@api_view(['GET'])
def servicesview(request):
    data = Services.objects.all()
    serial = ServicesSerializer(data, many=True)
    return Response(serial.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def galleryview(request):
    data = Gallery.objects.all()
    serail = GallerySerializer(data, many=True)
    return Response(serail.data, status=status.HTTP_200_OK)