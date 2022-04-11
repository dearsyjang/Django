from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
# 1. /accounts/ 유저 목록을 출력하는 페이지
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/index.html', context)

# 2. /accounts/signup/ 회원 가입 작성을 위한 페이지(유저 생성하는 기능 수행)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html', context)