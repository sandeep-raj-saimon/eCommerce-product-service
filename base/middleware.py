from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .utils import *
import jwt
SECRET_KEY= "ecommerceproject@1997"

class CustomerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            jwt_token = request.headers.get('authorization', None)
            if jwt_token:
                payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
                userid = payload.get('user_id', None)
                return None
            else:
                response = Response(
                    data={
                        'message': 'Missing Token'
                    },
                    status=status.HTTP_403_FORBIDDEN
                )
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response
        except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.InvalidTokenError):
            # return CustomResponse(message="Invalid Token").error_response()
            response = Response(
               data={
                   'message': 'Invalid Token'
               },
               status=status.HTTP_403_FORBIDDEN
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
        except (jwt.exceptions) as error:
            response = Response(
               data={
                   'message': error
               },
               status=status.HTTP_403_FORBIDDEN
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
        except Exception as error:
            response = Response(
               data={
                   'message': error
               },
               status=status.HTTP_403_FORBIDDEN
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
            
