from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
    # path('register/', registration_view, name='register')
]
