from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
# 1. Todo 목록
# 로그인 한 유저가 작성한 모든 todo 목록만을 보여준다.
# 만약 로그인 하지않은 경우 로그인 페이지로 redirect한다.
@login_required
def index(request):
    todos = Todo.objects.order_by('-pk')
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

# 2. Todo 생성
# 새로운 todo를 생선한다.
# 만약 로그인 하지않은 경우 로그인 페이지로 redirect한다.
@login_required
@require_http_methods(['GET','POST'])
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)