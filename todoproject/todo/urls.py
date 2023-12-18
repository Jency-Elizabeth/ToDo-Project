from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('',views.first_task,name='first_task'),
    #path('detail',views.detail,name='detail'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvtask/',views.Tasklistview.as_view(),name='cbvtask'),
    path('cbvdetails/<int:pk>/',views.Taskdeatailview.as_view(),name='cbvdetails'),
    path('cbvupdated/<int:pk>/',views.Taskupdatedview.as_view(),name='cbvupdated'),
    path('cbvdeleted/<int:pk>/',views.Taskdeletedview.as_view(),name='cbvdeleted'),
    ]