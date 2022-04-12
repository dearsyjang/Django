from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm


# Create your views here.
# 0. User List
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/index.html', context)

# 1. User Create 회원가입 기능
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 자동로그인
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html', context)


# 2. Login 로그인 기능
# nav: 로그인 한 유저 정보, 로그아웃, 회원수정, 회원탈퇴
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 로그인 인증
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


# 3. Logout 로그아웃 기능
# nav: 회원가입, 로그인
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)   
        return redirect('articles:index')


# 4. User Update 회원 정보 수정 기능
# 수정페이지: 이메일 주소, 이름, 성
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
        

# 5. User Delete 회원 삭제 기능
# POST method일 때만 삭제
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        # 해당 세션 데이터 지우기: 탈퇴 후, 로그아웃!
    return redirect('articles:index')


# workshop. User Change Password
@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)