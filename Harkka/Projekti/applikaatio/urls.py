from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.show_data, name='show_data'),
]