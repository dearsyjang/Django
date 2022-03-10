from django.urls import path
from . import views
# 처리해야할 목록
# articles/   : 모든 게시글 보여주기:index.html
# articles/new/ : 게시글 작성을 위한 양식 요청 new.html
# articles/create/ : 사용자가 작성한 내용을 DB에 저장
# articles/<int:pk>/ : pk에  해당하는 게시글 내용 보여주기 detail.html
app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
]