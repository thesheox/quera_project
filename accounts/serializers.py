from rest_framework import serializers
from .models import Benefactor, Charity

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
