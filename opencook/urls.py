"""opencook URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
admin.autodiscover()

from mainapp.views import get_index, get_signup, post_signup, post_login, post_logout,get_shop
from recipe.views import get_recipes_api, get_create_recipe, post_create_recipe, get_recipe

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup$', get_signup),
    url(r'^signup/post$', post_signup),
    url(r'^login/post$', post_login),
    url(r'^logout/post$', post_logout),
    url(r'^api/recipes$', get_recipes_api),
    url(r'^recipes/(\d+)$', get_recipe),
    url(r'^recipes/create$', get_create_recipe),
    url(r'^recipes/create/post$', post_create_recipe),
    url(r'^shop$', get_shop),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', get_index),

]
