from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^https://upadhyayans.github.io/$',views.homepage,name='homepage'),
]
