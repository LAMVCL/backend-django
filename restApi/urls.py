from django.urls import re_path
from restApi import views 

#Creamos las rutas que utilizaremos 
urlpatterns = [ 
    re_path(r'^api/$', views.todo_detail),
    re_path(r'^api/([0-9]+)$', views.todo_detail),
]