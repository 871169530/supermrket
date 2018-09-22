
from django.conf.urls import url

from super.views import login, cs, reg

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^reg/$', reg, name='reg'),
    url(r'^cs/$', cs, name='cs'),
]