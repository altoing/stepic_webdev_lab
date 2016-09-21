# coding=utf-8
"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#Сначало надо импортнуть view
#from qa.views import test, popular, question
#
#
#
#
#
#

from django.conf.urls import url
from django.contrib import admin
from qa.views import test, popular, question, mainpage, mainpage2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage2, name='mainpage'),
    url(r'^login/', test, name='test'),
    url(r'^signup/', test, name='test'),
    url(r'^question/(?P<id>\d+)', question, name='question'),
    url(r'^question/$', question, name='question'),
    url(r'^ask/', test, name='test'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='test'),
]
