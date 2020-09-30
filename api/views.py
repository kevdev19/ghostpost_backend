from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import RoastBoast
from .serializers import RoastBoastSerializer

class RoastBoastViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roast and boast content to be viewed and added
    """

    queryset = RoastBoast.objects.all()
    serializer_class = RoastBoastSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        upvote_obj = RoastBoast.objects.get(id=pk)
        serializer = RoastBoastSerializer(data=request.data)
        if serializer.is_valid():
            upvote_obj.up_vote = upvote_obj.up_vote + 1
            upvote_obj.save()
            return Response({'status': 'upvote set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        downvote_obj = RoastBoast.objects.get(id=pk)
        serializer = RoastBoastSerializer(data=request.data)
        if serializer.is_valid():
            # Convert negative number to positive number in Python
            # https://tinyurl.com/y5nlntbo
            downvote_obj.down_vote = downvote_obj.down_vote - 1
            downvote_obj.save()
            return Response({'status': 'downvote set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

