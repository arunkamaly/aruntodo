from django.contrib.auth.models import User

from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from list.models import  Todo
import datetime


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
    
@permission_classes((AllowAny, ))
class todolistView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def patch(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=kwargs['list_id'])
        todo.is_finished = True
        todo.finished_at = datetime.datetime.now()
        todo.save()

        result = {"status":True,"message":"updated successfully completed"}
        return Response(result, status=status.HTTP_200_OK)
