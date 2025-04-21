from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardView.as_view(), name='user_panel_dashboard'),
    path('edit-profile/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('change-pass/', views.ChangePasswordPageView.as_view(), name='change_password_page'),
]
