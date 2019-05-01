from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:eid>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:eid>/update/', views.update, name='update'),
    path('<int:eid>/delete/', views.delete, name='delete'),


]