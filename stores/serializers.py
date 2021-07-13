from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Pizzeria


class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'pizzeria_name',
            'city',
            'zip_code',
            # 'absolute_url'
        ]


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'pizzeria_name',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'email',
            'active'
        ]
