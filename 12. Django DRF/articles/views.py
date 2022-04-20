from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from articles.serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    # 모든 게시글의 id와 title 컬럼을 JSON 데이터 타입으로 응답한다.
    # 1. Article List
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # 검증에 성공하는 경우 새로운 게시글의 정보를 DB 저장하고, 저장된 게시글의 정보를 응답한다.
    # 검증에 실패한 경우 400 Bad Request 예외 발생
    # 2. Article Create
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 특정 게시글의 모든 컬럼을 JSON 데이터 타입으로 응답한다.
    # 3. Article Detail
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 특정 게시글의 정보를 수정한다.
    # 검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
    # 검증에 실패할 경우 400 Bad Request 예외를 발생시킨다.
    # 수정이 완료되면 수정한 게시글의 정보를 응답한다.
    # 4. Article Update
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    # 특정 게시글을 삭제한다.
    # 삭제가 완료되면 삭제한 게시글의 id를 응답한다.
    # 5. Article Delete
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
            



