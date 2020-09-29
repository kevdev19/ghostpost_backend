from rest_framework import serializers
from .models import RoastBoast

"""
RESOURCE:
Add a count field to a django rest framework serializer
https://tinyurl.com/y6aujsya
"""

class RoastBoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoastBoast
        fields = [
            'post_type',
            'content',
            'up_vote',
            'down_vote',
            'create_time',
            'update_time',
            ]