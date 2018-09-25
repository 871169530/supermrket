from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from db.base_view import BaseVerifyView
from super.forms import RegisterForm, LoginForm

# Create your views here.

# 登录
# from super.helper import verify_login_required
from super.models import Users


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
        session_code = request.session.get('random_code')
        form = RegisterForm(request.POST)
        data = request.POST.dict()
        data['session_code'] = session_code
        form = RegisterForm(data)
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


class SendCodeView(View):
    # 发送短信验证码
    def post(self, request):
        # 接收
        phone = request.POST.get("tel", "")
        # 处理
        import re

        phone_re = re.compile("^1[3-9]\d{9}$")
        res = re.search(phone_re, phone)
        if res is None:
            # 手机号码格式错误
            return JsonResponse({"status": "400", "msg": "手机号码格式错误"})

        res = Users.objects.filter(phone=phone).exists()
        if res:
            # 手机号码格式错误
            return JsonResponse({"status": "400", "msg": "手机号码已经注册"})
        # 生成随机验证码
        import random
        random_code = "".join([str(random.randint(0, 9)) for _ in range(4)])
        # 模拟发送
        print("=code={}=".format(random_code))

        request.session['random_code'] = random_code
        request.session.set_expiry(60)

        # 响应
        return JsonResponse({"status": "200"})
