"""futureerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.auth.models import User

import dashboard.views as dashboard_views
import reg.views as reg_views
import api.views as api_views

from rest_framework import routers, serializers, viewsets


# serializers define the api representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# routers provide an easy way of automatically determining the url conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', dashboard_views.home, name='home'),

    # auth URL confs
    url(r'^login/$', dashboard_views.login_page, name='login_page'),
    url(r'^logout/$', dashboard_views.logout_page, name='logout_page'),
    url(r'^accounts/logout/$', dashboard_views.logout_page, name='logout_page'),
    url(r'^accounts/login/$', dashboard_views.login_page, name='login_page'),

    # registration
    url(r'register/$', reg_views.regform, name='regform'),

    # django rest framework urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^products/$', api_views.product_list),
    url(r'^products/(?P<pk>[0-9]+)/$', api_views.product_detail),

    # apis for notes - category and notes models
    url(r'^notes/categories/(?P<user_id>[0-9]+)/$', api_views.category_list),
    url(r'^notes/categories/(?P<user_id>[0-9]+)/(?P<pk>[0-9]+)/$', api_views.category_detail),
    url(r'^notes/notes/$', api_views.note_list),
    url(r'^notes/notes/(?P<pk>[0-9]+)/$', api_views.note_detail),
]
