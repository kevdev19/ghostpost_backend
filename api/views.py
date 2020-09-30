from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import RoastBoast
from .serializers import RoastBoastSerializer

class RoastBoastViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roast and boast content to be viewed and added
    """

    queryset = RoastBoast.objects.all()
    serializer_class = RoastBoastSerializer
