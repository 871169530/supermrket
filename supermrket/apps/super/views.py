from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from super.forms import RegisterForm, LoginForm


# Create your views here.


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, "Supermarket/login.html", {'form': login_form})

    def post(self, request):
        login_from = LoginForm(request.POST)
        if login_from.is_valid():
            return redirect(reverse('super:member'))
        return render(request, 'Supermarket/login.html', {'form': login_from})


class RegisterView(View):
    """
        # 注册
    """

    def get(self, request):
        # 创建注册表单对象
        register_form = RegisterForm()
        return render(request, "Supermarket/reg.html", {"form": register_form})

    def post(self, request):
        # 接收数据
        # 处理数据
        # 响应
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # 注册成功，跳转
            return redirect(reverse('super:login'))
        return render(request, 'Supermarket/reg.html', {'form': form})


def member(request):
    return render(request, 'Supermarket/member.html')


def cs(request):
    return HttpResponse('ok')
