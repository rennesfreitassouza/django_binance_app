from django.urls import path, re_path
from . import views


urlpatterns = [
    path('execute_new_req/', views.execute_new_req, name='execute_new_req'),
    re_path(r'^exec_request[/]?$', views.exe, name='RESTful_Web_API'),
]
