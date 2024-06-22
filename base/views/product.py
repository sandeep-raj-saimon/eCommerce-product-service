from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..documents import *
from ..utils import *

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        # return HttpResponse('Creating Product')
        try:
            query_param = request.GET.get("q")
            if query_param:
                categories = ProductDocument.search().query("match", description=query_param).to_queryset()
                if categories:
                    return Response(categories)
            return Response({
                "msg": "No such product found"
            })
        except Exception as e:
            print('error is {}', e)
            return HttpResponse('No such product found')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Creating Product')
    
    def put(self, request, *args, **kwargs):
        return HttpResponse('Updating Product')
    
    def delete(self, request, *args, **kwargs):
        return HttpResponse('Deleting Product')