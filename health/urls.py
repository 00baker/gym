from django.conf.urls import url
from health import views

urlpatterns = [
    url(r'^$', views.health,name='health'),
    url(r'^(?P<slug>[\w-]+)/$', views.health_post, name='view_health_post'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.health_category, name='view_health_category')
]

