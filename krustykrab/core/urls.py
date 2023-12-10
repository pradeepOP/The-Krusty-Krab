from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home" ),
   path('about/',views.about, name="about" ),
   path('signup/',views.signup, name="signup" ),
   path('login/',views.loginView, name="login" ),
   path('logout/',views.logoutView, name="logout" ),
   path('review/', views.review, name="review"),
   path('menu/', views.menu, name="menu"),
   path('account/', views.account, name="account"),
   path('edit_account/', views.edit_account, name="edit-account"),
    
]
