from django.conf.urls import include, url
from core import views as c

urlpatterns = [
    url(r'^$', c.home, name='home'),
]
