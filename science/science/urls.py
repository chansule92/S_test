from django.urls import path

from . import views

urlpatterns = [
    path('1/', views.menu1),
    path('1_1/',views.menu1_1),
    path('1_2/',views.menu1_2),
    path('2_1/',views.menu2_1),
    path('2_2/',views.menu2_2),
    path('2_3/',views.menu2_3),
    path('3_1/',views.menu3_1),
    path('3_2/',views.menu3_2),
    path('3_3/',views.menu3_3),
    path('4_1/',views.menu4_1),
    path('4_2/',views.menu4_2),
]
