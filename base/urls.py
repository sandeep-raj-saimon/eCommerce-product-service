from django.urls import path
from django.http import HttpResponse
# from . import views
from .views import *

def home(request):
    return HttpResponse('Home Page')

urlpatterns = [
    path('', home, name = "home"),
    path('product/', ProductView.as_view()),
    path('category/', CategoryView.as_view())
]