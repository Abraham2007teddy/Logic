from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'question')  # Display fields in the admin panel
    search_fields = ('name', 'email')  # Enable search
    list_filter = ('email',)  # Filter messages by email
