from django.urls import path
from . import views
urlpatterns=[
    path('',views.apiCreated,name='apiCreated'),
    path('User/',views.UserCreated,name='UserCreated'),
    path('check/'),
]