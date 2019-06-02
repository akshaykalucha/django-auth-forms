from django.urls import path
from . import views
import re
urlpatterns = [
    path('', views.index, name='index'),
]