from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from db.base_view import BaseVerifyView
from super.forms import RegisterForm, LoginForm


# Create your views here.

# 登录
# from super.helper import verify_login_required


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, "Supermarket/login.html", {'form': login_form})

    def post(self, request):
        login_from = LoginForm(request.POST)
        if login_from.is_valid():
            user = login_from.cleaned_data.get('user')
            request.session['ID'] = user.pk
            request.session['phone'] = user.phone
            request.session.set_expiry(0)

            return redirect(reverse('super:center'))
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


class CenterView(BaseVerifyView):
    def get(self, request):
        phone = request.session.get('phone')
        context = {
            'phone': phone
        }
        return render(request, 'Supermarket/member.html', context)


class InforView(BaseVerifyView):
    def get(self, request):
        # 验证用户是否登录
        # 判断 session
        # user_id = request.session.get('ID')
        # if user_id is None:
        #     # 没有登录转到登录页面
        #     return redirect(reverse('super:login'))
        return render(request, 'Supermarket/infor.html')

    # @method_decorator(verify_login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

# @verify_login_required
# def info(request):
#     return render(request, 'Supermarket/infor.html')
