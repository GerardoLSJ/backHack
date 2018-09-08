from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from firebase_admin import auth
from rest_framework import viewsets

from .serializers import(TagsSerializer, ProcedureSerializer,
                         LawSerializer, CitySerializer,
                         CountrySerializer)

from .models import(Tags, Procedure, Law, City, Country)

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class TestView(View):
    def get(self, request, *args, **kwargs):
        # id_token comes from the client app (shown above)
        id_token = request.META['HTTP_AUTHORIZATION']
        print('wwwwwooooooowwwww : ')
        print(id_token)

        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        print('uid')
        print(uid)
        print('uid')
        return HttpResponse('hello', content_type='application/json')

    def post(self, request, *args, **kwargs):
        # data = request.body.decode("utf-8") 
        # for key, value in request.POST.items():
        #     print(key, value)
        
        # print('hello ___')
        # print(data)

        # pdf = render_to_pdf(data)
        return HttpResponse(pdf, content_type='application/json')

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class LawViewSet(viewsets.ModelViewSet):
    queryset = Law.objects.all()
    serializer_class = LawSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
