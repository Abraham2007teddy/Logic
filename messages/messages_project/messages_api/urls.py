from django.urls import path
from .views import MessageCreateView, MessageListView, MessageDeleteView

urlpatterns = [
    path('send-message/', MessageCreateView.as_view(), name='send-message'),
    path('get-messages/', MessageListView.as_view(), name='get-messages'),
    path('delete-message/<int:pk>/', MessageDeleteView.as_view(), name='delete-message'),
]
