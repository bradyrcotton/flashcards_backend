from django.shortcuts import render
from .models import Card, Collection
from .serializers import CardSerializer, CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CardList(APIView):

    def get(self, request):
        card = Collection.objects.all()
        serializer = CollectionSerializer(card, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionList(APIView):

    def get(self, request):
        card = Collection.objects.all()
        serializer = CollectionSerializer(card, many=True)
        return Response(serializer.data)