from django.views import View
from django.http import HttpResponse
from ..models import *
from ..documents import *

class ProductView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Getting Product')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Creating Product')
    
    def put(self, request, *args, **kwargs):
        return HttpResponse('Updating Product')
    
    def delete(self, request, *args, **kwargs):
        return HttpResponse('Deleting Product')