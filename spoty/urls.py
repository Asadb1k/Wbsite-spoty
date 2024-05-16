from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage,name='home'),
    path('song/<int:id>/', views.Private,name='song'),
    path('category/<int:id>/', views.CategoryPage.as_view(),name='category'),
    path('login/', views.Login,name='login'),
    path('logout/', views.LogoutPage,name='logout'),
    path('SignUp/', views.SignUp,name='SignUp'),
]
