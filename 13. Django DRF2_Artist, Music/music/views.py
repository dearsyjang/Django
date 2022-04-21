from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from music import serializers

from music.serializers import ArtistListSerializer, ArtistSerializer, MusicSerializer
from .models import Artist, Music


# Create your views here.
@api_view(['GET','POST'])
def artist_list(request):
    # 모든 가수의 id와 name 컬럼을 JSON으로 응답한다.
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    # 가수의 정보를 생성한다.
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET'])
# 특정 가수의 모든 컬럼을 JSON으로 응답한다.
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


@api_view(['POST'])
# 특정 가수의 음악 정보를 생성한다.
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# 모든 음악의 id와 title 컬럼을 JSON으로 응답한다.
def music_list(request):
    musics = get_list_or_404(Music)
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    # 특정 음악의 모든 컬럼을 JSON으로 응답한다.
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    # 특정 음악의 정보를 수정한다.
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    # 특정 음악의 정보를 삭제한다.
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번이 삭제되었습니다!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    






    




        
