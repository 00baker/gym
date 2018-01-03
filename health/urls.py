from django.conf.urls import url
from health import views

urlpatterns = [
    url(r'^$', views.index,name='health'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[\w-]+)/$', views.view_category, name='view_blog_category')
]

