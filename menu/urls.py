from django.conf.urls import url

from menu import views


urlpatterns = [
    url(r'^$', views.menu, name='menu'),

]
