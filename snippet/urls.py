
from django.urls import path

from . import views

urlpatterns = [
    path('over', views.OverView, name='OverView'),
    path('create', views.createPost, name='crete'),
    path('listdetail',views.ListDetail, name='detail'),
    path('itemdetail/<str:pk>', views.BlogDetail,  name='BlogDetail'),
    path('updateblog/<str:pk>', views.BlogUpdate,  name='BlogDetail'),
    path('delete/<str:pk>',views.BlogDelete,name="blogdlete")
    


]