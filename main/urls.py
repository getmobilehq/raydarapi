from django.urls import path 
from . import views


urlpatterns = [
    path("inventories/", views.InventoryListCreate().as_view())
]
