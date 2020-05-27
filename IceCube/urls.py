"""IceCube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from IceCube import views
from accounts import urls
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


# anything at top of your browser is defined here


urlpatterns = [

    path('',views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
# link app urls to master urls
    path('account/', include('accounts.urls')),



#   set path_to_there('word_in_address_bar/', funct_to_get_there(display_this),

]
