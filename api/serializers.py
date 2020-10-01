from rest_framework import serializers
from .models import RoastBoast

"""
RESOURCE:
Add a count field to a django rest framework serializer
https://tinyurl.com/y6aujsya
https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
"""

class RoastBoastSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = RoastBoast
        # fields = '__all__'
        fields = [
            'id',
            'post_type',
            'content',
            'up_vote',
            'down_vote',
            'create_time',
            'update_time',
            'total_votes',
            ]

    
    total_votes = serializers.SerializerMethodField()
    def get_total_votes(self, obj):
        return (obj.up_vote - obj.down_vote)
