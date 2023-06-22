from rest_framework import serializers

from .models import Worker


class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["id", "name", "surname", "birth_date", "phone_number", "working_since", "gender"]


class WorkerCreateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
