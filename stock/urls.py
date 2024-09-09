from django.urls import path
from .views import StockListCreate, StockRetrieveUpdateDestroy

urlpatterns = [
    path('stocks/', StockListCreate.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroy.as_view(), name='stock-retrieve-update-destroy'),
]
