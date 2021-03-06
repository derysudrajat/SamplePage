"""SamplePage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

from about import views as viewAbout
from list import views as viewList
from sampleapp import views as viewSample


def profile(request):
    return HttpResponse("<h1>This is Profile page</>")


urlpatterns = [
    url(r'^sampleapp', include('sampleapp.urls')),
    url(r'^$', viewSample.home),
    url(r'^profile/', profile),
    url(r'^todolist/', viewList.index),
    url(r'^admin/', admin.site.urls),
    url(r'about/$', viewAbout.index)
]
