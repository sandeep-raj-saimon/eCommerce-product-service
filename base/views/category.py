from django.views import View
from django.http import HttpResponse
from ..models import *
from ..documents import *

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        query_param = request.GET.get("q")
        if query_param:
            categories = CategoryDocument.search().query("match", description=query_param)
            if categories:
                return HttpResponse(categories)
        return HttpResponse('No Such Category found')

    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Creating Category')
    
    def put(self, request, *args, **kwargs):
        return HttpResponse('Updating Category')
    
    def delete(self, request, *args, **kwargs):
        return HttpResponse('Deleting Category')