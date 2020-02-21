from . models import AndelaEngineer, PartnerEngineer
from rest_framework import serializers


class AndelaEngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndelaEngineer
        fields = ('id', 'name', 'level')


class PartnerEngineerSerializer(serializers.ModelSerializer):
    engineer_id = serializers.IntegerField(write_only=True)
    engineer = AndelaEngineerSerializer(read_only=True)
    class Meta:
        model = PartnerEngineer
        fields = ('id', 'level', 'engineer_id', 'engineer')






