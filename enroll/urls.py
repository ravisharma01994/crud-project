from django.urls import path

from . import views

urlpatterns=[
    path('',views.add_show,name='show'),
    path('delete/<int:id>/',views.delete_data,name='erase'),
    path('<int:id>/',views.update_data, name='new'),
    
]