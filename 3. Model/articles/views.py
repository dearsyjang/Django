from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    #여기에서 DB의 게시글 데이터를 가져와야 합니다. 
    articles = Article.objects.all()[::-1]
    # 게시글 정렬 최신순
    # articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

#사용자가 내용을 작성하기 위해 보여주는 양식
def new(request):
    return render(request,'articles/new.html')

#사용자가 작성한 내용을 저장하면 됩니다. 
def create(request):
    #사용자가 보낸 데이터를 받아서 DB에 저장
    # save()
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    # Article.objects.create(title=title, content=content)

    article = Article()
    article.title = title
    article.content = content
    article.save()
    # article = Article(title=title, content=content)
    # article.save()
    # return render('articles/create.html')
    return redirect('articles:detail', article.pk)

def detail(request,pk):
    #pk를 아니까.....DB에서 가져오기
    article = Article.objects.get(pk=pk)
    context ={
        'article' : article
    }
    return render(request,'articles/detail.html',context)
