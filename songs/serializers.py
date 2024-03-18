from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Song
        fields = ['id', 'title', 'duration', 'album_id']
        extra_fields = {'id': {'read_only': True}, 'album_id': {'read_only': True}}
        depth = 1

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
