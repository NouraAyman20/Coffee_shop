from django.urls import path
from . import views
app_name='coffee'

urlpatterns=[
  path('home' , views.home,name='coffee_store'),
  path('' ,views.main,name='main'),
  path('add/<int:coffee_id>/', views.detail, name='detail'),
]




