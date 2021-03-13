from django.urls import path
from . import views

urlpatterns = [
    path('mike',views.index,name="index")
]