from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:user_list_id>/', views.start, name='start'),

]
