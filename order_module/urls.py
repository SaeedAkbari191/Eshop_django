from django.urls import path,include
from . import views

urlpatterns = [
    path('add-to-order', views.add_to_order, name='add_to_order'),
]
