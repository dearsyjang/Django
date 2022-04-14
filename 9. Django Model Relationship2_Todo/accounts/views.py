from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods, require_POST



# Create your views here.
# 0. User List
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users':users,
    }
    return render(request, 'todos/index.html', context)

# 1. 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 자동로그인
            auth_login(request,user)
            return redirect('todos:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html', context)


# 2. 로그인
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


# 3. 로그아웃
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)   
        return redirect('todos:index')