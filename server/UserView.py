from django import forms

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from server.models import SuperHero
from server.serializers import SuperHeroSerializer


class NameForm(forms.Form):
    name = forms.CharField(label='Nome do heroi', max_length=100)
    description = forms.CharField(label='Breve descrição do heroi', max_length=100)
    photo = forms.FileField()
    favorite = forms.BooleanField(required=False)

def index(request):
    super_heroes = SuperHero.objects.filter(favorite=True)
    form = NameForm()
    return render(request, "index.html", {'form': form,'super':super_heroes})

class SuperHeroView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self,request):

        print(request.POST.get("name"))
        print(request.data)

        file_serializer = SuperHeroSerializer(data=request.data)

        if file_serializer.is_valid():

            file_serializer.validated_data['alias'] = request.POST.get("name").replace(" ","%")
            file_serializer.save()
            super_heroes = SuperHero.objects.filter(favorite=True)
            form = NameForm()
            return render(request, "index.html", {'form': form,'super':super_heroes})
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,superhero_id='',format=None):


        try:
            if superhero_id is not '':
                super_hero = SuperHero.objects.get(id=superhero_id)
                file_serializer = SuperHeroSerializer(super_hero)
            else:
                super_hero = SuperHero.objects.filter(favorite=True)
                file_serializer = SuperHeroSerializer(super_hero,many=True)
            response = {'super_hero': file_serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self, request,superhero_id):

        super_hero = SuperHero.objects.get(id=superhero_id)

        request_serializer = SuperHeroSerializer(super_hero, data=request.data)
        if request_serializer.is_valid():
            request_serializer.save()
            return Response(request_serializer.data)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,superhero_id):

        SuperHero.objects.get(id=superhero_id).delete()
        payload = {'success': True}
        return Response(json.dumps(payload),status=status.HTTP_200_OK)



class FilterSuperHeroView(APIView):

    def post(self,request):

        try:

            super_hero = SuperHero.objects.get(name=request.POST.get("name"))
            file_serializer = SuperHeroSerializer(super_hero)
            response = {'super_hero': file_serializer.data}

            return Response(response, status=status.HTTP_200_OK)

        except:

            return Response(status=status.HTTP_404_NOT_FOUND)

