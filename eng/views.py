from rest_framework import viewsets
from . serializers import AndelaEngineerSerializer, PartnerEngineerSerializer
from .models import AndelaEngineer, PartnerEngineer


class IndexViewSet(viewsets.ModelViewSet):
    queryset = AndelaEngineer.objects.all()
    serializer_class = AndelaEngineerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = PartnerEngineer.objects.all()
    serializer_class = PartnerEngineerSerializer
