from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from ..models import *
from ..documents import *
from ..utils import *

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            query_param = request.GET.get("q")
            if query_param:
                product = ProductDocument.search().query("match", description=query_param).to_queryset()
                if product:
                    return CustomResponse(data=product).success_response()
            return CustomResponse(message="No such product found").error_response()
        except Exception as e:
            print('error is {}', e)
            return CustomResponse(message="No such product found").error_response()
    
    def post(self, request, *args, **kwargs):
        return CustomResponse(message='Creating Product').success_response()
    
    def put(self, request, *args, **kwargs):
        return CustomResponse(message='Updating Product').success_response()
    
    def delete(self, request, *args, **kwargs):
        return CustomResponse(message='Deleting Product').success_response()