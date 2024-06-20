from django.views import View
from django.http import HttpResponse
from ..models import *
from ..documents import *
from ..utils import *

class ProductView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse('Creating Product')
        try:
            query_param = request.GET.get("q")
            if query_param:
                categories = ProductDocument.search().query("match", description=query_param).to_queryset()
                if categories:
                    return HttpResponse(categories)
            return HttpResponse('No such product found')
        except Exception as e:
            print('error is {}', e)
            return HttpResponse('No such product found')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Creating Product')
    
    def put(self, request, *args, **kwargs):
        return HttpResponse('Updating Product')
    
    def delete(self, request, *args, **kwargs):
        return HttpResponse('Deleting Product')