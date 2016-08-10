from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.issue_list, name='issue_list'),
    url(r'^post/(?P<pk>\d+)/$', views.issue_detail, name='issue_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.issue_remove, name='issue_remove'),

]
