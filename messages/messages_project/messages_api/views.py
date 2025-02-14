from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

# API to create a new message
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# API to retrieve all messages
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all().order_by('-id')  # Order by latest message
    serializer_class = MessageSerializer

# API to delete a message
class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
