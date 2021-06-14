from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.sign_up_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
]