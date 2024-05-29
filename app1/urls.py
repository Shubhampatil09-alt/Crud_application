from django.urls import path
from . import views
urlpatterns =[
    path('server_list/', views.server_list, name='server_list'),

]