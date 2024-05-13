from django.urls import re_path as url
from . import views

app_name = 'CategoryApp'

urlpatterns = [
    url(r'', views.category, name="category"),
]
