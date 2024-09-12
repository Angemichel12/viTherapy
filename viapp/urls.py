from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/record_weight/', views.record_weight, name='record_weight'),
    path('api/get_iv_percentage/', views.get_iv_percentage, name='get_iv_percentage'),
]