from django.urls import path, include
from . import views

urlpatterns=[ 
    path('thread/',views.thread,name='thread'),
    path('',views.forum,name='forum'),
    path('single_thread/<int:pk>',views.single_thread,name='singlethread')
]