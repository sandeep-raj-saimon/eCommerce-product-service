from django.http import *
class CustomResponse:

    def __init__(self, data):
        self.data = data

    def success_response(self):
        return HttpResponse({
            "data": self.data
        })

    def error_response(self):
        return HttpResponseServerError()