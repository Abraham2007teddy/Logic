from django.urls import path
from .views import CargoRequestListCreate, CargoRequestDetail

urlpatterns = [
    path('cargo-requests/', CargoRequestListCreate.as_view(), name='cargo-request-list-create'),
    path('cargo-requests/<str:pk>/', CargoRequestDetail.as_view(), name='cargo-request-detail'),  
]