from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from server.models import SuperHero


class SuperHeroSerializer(ModelSerializer):
    class Meta:
        model = SuperHero
        fields = '__all__'
