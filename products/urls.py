from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^products/$', views.ProductsListView.as_view()),
    url(r'^products/(?P<pk>[0-9])$', views.ProductsDetailView.as_view()),
    url(r'^products/add/(?P<pk>[0-9])$', views.add_to_follow_list, name='add-to-follow'),
]
