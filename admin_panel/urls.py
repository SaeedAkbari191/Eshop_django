from django.urls import path
from . import views

urlpatterns = [
    path('', views.Admin_Dashboard.as_view(), name='admin_dashboard'),
    path('products/', views.ProductListView.as_view(), name='product_list_admin'),
    path('products/<int:pk>', views.ProductEditView.as_view(), name='product_edit_admin'),
]
