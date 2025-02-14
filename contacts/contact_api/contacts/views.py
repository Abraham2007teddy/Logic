from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

# List & Create API (GET, POST)
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Retrieve, Update & Delete API (GET, PUT, DELETE)
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
