from django.urls import path, include
from . import views

app_name = 'home_app'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('SuccessViewHome/', views.SuccessViewHome.as_view(),name ='correct'),
    path('add-home', views.HomeCreateView.as_view(), name='add-home'),
    path('test', views.TestViewHome.as_view(), name='test'),
    path('navbar', views.NavbarViewHome.as_view(), name='navbar'),
    path('menu', views.MenuViewHome.as_view(), name='menu'),
    path('footer', views.footerViewHome.as_view(), name='footer'),
]
