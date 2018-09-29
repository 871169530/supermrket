
from django.conf.urls import url

from good.views import IndexView
from super.views import (RegisterView,
                         LoginView,
                         CenterView,
                         InforView,
                         SendCodeView)

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', IndexView.as_view(), name='主页'),
    url(r'^reg/$', RegisterView.as_view(), name='register'),
    url(r'^member/$', CenterView.as_view(), name='center'),
    url(r'^infor/$', InforView.as_view(), name='info'),
    url(r'^SendCodeView/$', SendCodeView.as_view(), name='SendCodeView'),
]
