"""bandsite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.edit import CreateView
from forms import SignupForm


urlpatterns = [
	url(r'^bandmanager/', include('bandmanager.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', CreateView.as_view(
        template_name='signup.html',
        form_class=SignupForm,
        success_url='/bandmanager/band/'
    ), name='signup'),
    url('^accounts/', include('django.contrib.auth.urls')),
]
