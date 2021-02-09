from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from django.utils.safestring import mark_safe

from server.models import SuperHero


class NameForm(forms.Form):
    name = forms.CharField(label='Nome do heroi', max_length=100)
    description = forms.CharField(label='Breve descrição do heroi', max_length=100)
    photo = forms.FileField()
    favorite = forms.BooleanField(required=False)

def index(request):
    # return HttpResponse('Hello from Python!')
    super_heroes = SuperHero.objects.filter(favorite=True)
    form = NameForm()
    return render(request, "index.html", {'form': form, 'super': super_heroes})

