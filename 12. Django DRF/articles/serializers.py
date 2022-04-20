from rest_framework import serializers
from .models import Article

# 모든 게시글 정보 반환: id, title
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields =('id', 'content',)

# 게시글 상세 정보를 반환 및 생성: 모든 field
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
