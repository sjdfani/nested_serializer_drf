from rest_framework import serializers
from django.contrib.auth import get_user_model
from address.serializer import AddressSerializer
from address.models import Address


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = get_user_model()
        exclude = ['password']
        # fields='__all__'

    def create(self, validated_data):
        addresses = validated_data.pop('addresses')
        user = get_user_model().objects.create(**validated_data)
        for address in addresses:
            Address.objects.create(user=user, **address)
        return user
