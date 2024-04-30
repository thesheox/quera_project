from rest_framework import serializers
from charities.models import Benefactor, Charity
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
        return Benefactor.objects.create(user=user, **validated_data)

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ['name', 'reg_number']

    def create(self, validated_data):
        user = self.context['request'].user
        return Charity.objects.create(user=user, **validated_data)
