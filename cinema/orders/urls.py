from django.conf.urls import url
from orders import views


urlpatterns = [
    url(r'^orders/$', views.order_list, name='order_list'),
    url(r'^orders/(?P<id>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^sessions/(?P<id>[0-9]+)/$', views.session_detail, name='session_detail'),
    url(r'^films/$', views.film_list, name='film_list'),
    url(r'^films/(?P<id>[0-9]+)/$', views.film_detail, name='film_detail'),
]