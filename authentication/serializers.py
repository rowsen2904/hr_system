from rest_framework import serializers

from .models import UserData


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "username"]
