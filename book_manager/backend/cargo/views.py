# views.py
from rest_framework import generics
from .models import CargoRequest
from .serializers import CargoRequestSerializer

class CargoRequestListCreate(generics.ListCreateAPIView):
    queryset = CargoRequest.objects.all()
    serializer_class = CargoRequestSerializer

class CargoRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CargoRequest.objects.all()
    serializer_class = CargoRequestSerializer