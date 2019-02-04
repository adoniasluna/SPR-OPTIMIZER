from django.urls import path

from . import views

urlpatterns = [
    # ex: /spr_optimizer/
    path('', views.index, name='index'),
    path('uploading/', views.upload, name='uploading'),
    path('setting/', views.setting, name='setting'),
    path('help/', views.get_help, name='help'),
    path('uploading/optimize/', views.optimize, name='optimize')
]
