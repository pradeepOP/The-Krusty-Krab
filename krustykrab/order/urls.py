from django.urls import path
from . import views
urlpatterns = [
    path('start_order/', views.start_order, name="start-order"),
]
