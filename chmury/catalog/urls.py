from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index,name="index"),
    path('view',views.view,name="data_view"),
    path('add',views.view,name="data_add")
]
