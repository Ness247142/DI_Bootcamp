from django.urls import path
from . import views

urlpatterns = [
    path('add_gif/', views.add_gif, name='add_gif'),
    path('add_category/', views.add_category, name='add_category'),
    path('view_gif/<int:id>', views.view_gif, name='view_gif'),
    path('view_categories/', views.view_categories, name='view_categories'),
    path('view_category/<int:id>', views.view_category, name='view_category'),
    path('', views.homepage, name='homepage'),
]
