from django.http import Http404
from rest_framework import viewsets, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import AndelaEngineerSerializer, PartnerEngineerSerializer
from .models import AndelaEngineer, PartnerEngineer


class CreateEngView(APIView):
    def post(self, request):
        serializer = AndelaEngineerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CreatePartnerView(APIView):
    def post(self, request):
        serializer = PartnerEngineerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GetEngView(APIView):
    def get_object(self, pk):
        try:
            return AndelaEngineer.objects.get(pk=pk)
        except AndelaEngineer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        eng = self.get_object(pk)
        serializer = AndelaEngineerSerializer(eng)
        return Response(serializer.data)


class GetPartnerView(APIView):
    def get_object(self, pk):
        try:
            return PartnerEngineer.objects.get(pk=pk)
        except PartnerEngineer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        eng = self.get_object(pk)
        serializer = PartnerEngineerSerializer(eng)
        return Response(serializer.data)
