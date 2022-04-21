from rest_framework import serializers
from .models import Artist, Music


# 모든 가수의 정보를 반환
class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)


# 상세 음악의 정보를 생성 및 반환
class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)


# 상세 가수의 정보를 생성 및 반환
class ArtistSerializer(serializers.ModelSerializer):

    music_set = MusicSerializer(many=True, read_only=True)

    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'




