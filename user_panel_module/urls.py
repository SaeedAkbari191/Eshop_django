from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardView.as_view(), name='user_panel_dashboard'),
    path('edit-profile/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('settings/', views.ChangePasswordPageView.as_view(), name='setting_page'),
    path('user-basket/', views.UserBasket.as_view(), name='user_basket_page'),
    path('my-shopping/', views.MyShoppingPage.as_view(), name='user_shopping_page'),
    path('my-shopping-details/<order_id>', views.my_shopping_details, name='user_shopping_details_page'),
    path('remove-order-detail/', views.remove_order_detail, name='remove_order_detail_page'),
    path('change-order-detail/', views.changeOrderDetailCount, name='change_order_detail_page'),
    # path('payment/',views.payment_view, name='payment_page'),
    path('payment-success/', views.payment_success, name='payment_success_page'),
    path('payment-failure/', views.payment_failure, name='payment_failure_page'),
    path('paypal/', include("paypal.standard.ipn.urls")),

]
