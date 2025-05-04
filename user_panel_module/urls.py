from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardView.as_view(), name='user_panel_dashboard'),
    path('edit-profile/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('settings/', views.ChangePasswordPageView.as_view(), name='setting_page'),
    path('user-basket/', views.user_basket, name='user_basket_page'),

]
