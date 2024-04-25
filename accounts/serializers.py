from rest_framework import serializers

from charities.models import Charity, Benefactor
from .models import User
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('username','password','phone','address','gender','age','description','first_name','last_name','email')
    def create(self, validated_data):
        the_user = User.objects.create_user(**validated_data)
        return the_user


class BenefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = ['experience', 'free_time_per_week']

    def create(self, validated_data):
        user = self.context['request'].user
        benefactor = Benefactor.objects.create(user=user, **validated_data)
        return benefactor


class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ['name', 'reg_number']

    def create(self, validated_data):
        user = self.context['request'].user
        charity = Charity.objects.create(user=user, **validated_data)
        return charity
