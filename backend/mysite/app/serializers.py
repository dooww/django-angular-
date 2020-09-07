from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Condidat
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CondidatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Condidat
        fields=['pk','first_name','last_name','birthday','cv','phone_numbr','e_mail']
