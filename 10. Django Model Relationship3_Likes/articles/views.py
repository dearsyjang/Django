from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import render, redirect, get_object_or_404

from accounts.views import login


from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    article = form.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm(instance=article)
            context = {
                'article': article,
                'form': form,
            }
            return render(request, 'articles/update.html', context)


# 좋아요
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # 좋아요 누른 users 목록에 현재 요청한 user가 있으면, 좋아요 취소!
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        # 없다면, 좋아요 누른 users 목록에 추가, 좋아요!
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')


