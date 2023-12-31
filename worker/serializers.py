from rest_framework import serializers

from .models import Worker


class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["id", "fullname", "birth_date", "phone_number", "working_since", "gender"]


class WorkerAllFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
