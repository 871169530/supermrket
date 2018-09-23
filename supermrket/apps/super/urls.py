
from django.conf.urls import url

from super.views import RegisterView, LoginView, CenterView, InforView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^reg/$', RegisterView.as_view(), name='register'),
    url(r'^member/$', CenterView.as_view(), name='center'),
    url(r'^infor/$', InforView.as_view(), name='info'),
]
