
from django.conf.urls import url

from super.views import cs, RegisterView, LoginView, member

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^reg/$', RegisterView.as_view(), name='register'),
    url(r'^member/$', member, name='member'),
]