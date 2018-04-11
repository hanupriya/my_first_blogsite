from django.conf.urls import url
from . import views


''' url paterns '''

urlpatterns = [ url(r'^$',views.post_list, name = 'post_list'),
               ]

