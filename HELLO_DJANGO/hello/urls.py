from django.urls import path

from . import views
from hello import viewssample

urlpatterns = [
    path('', views.hello, name='index'),
    path('param', views.param, name='param'),
    path('dispa', views.dispa, name='dispa'),
    path('emp', views.emp, name='emp'),
    path('ajax', views.ajax, name='ajax'),
    path('ajax_insert', views.ajax_insert, name='ajax_insert'),
    path('ajax_update', views.ajax_update, name='ajax_update'),
    path('ajax_delete', views.ajax_delete, name='ajax_delete'),
    path('sample', viewssample.smp, name='smp'),
    path('smp_insert', viewssample.smp_insert, name='smp_insert'),
    path('smp_update', viewssample.smp_update, name='smp_update'),
    path('smp_delete', viewssample.smp_delete, name='smp_delete'),
    path('ajax_sync', viewssample.ajax_sync, name='ajax_sync'),
    path('axios_sync', viewssample.axios_sync, name='axios_sync'),
]