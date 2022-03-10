from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    content = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', content)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context ={
        'article' : article
    }
    return render(request,'articles/detail.html',context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')
    

