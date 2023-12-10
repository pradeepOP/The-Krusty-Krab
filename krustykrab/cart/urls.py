from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:menuItem_id>/',views.add_to_cart, name="add-to-cart" ),
    path('', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('hx_menu_cart/', views.hx_menu_cart, name="hx_menu_cart"),
    path('update_cart/<int:menuItem_id>/<str:action>/', views.update_cart, name="update-cart"),
    path('hx_cart_total/', views.hx_cart_total, name="hx_cart_total"),
    
    
]
