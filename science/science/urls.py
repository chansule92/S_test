from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('question0/', views.question0, name='question0'),
    path('question1/', views.question1, name='question1'),
    path('question1_1/', views.question1_1, name='question1_1'),
    path('question2/', views.question2, name='question2'),
    path('question2_1/', views.question2_1, name='question2_1'),
    path('final0/', views.final0, name='final0'),
    path('final1/', views.final1, name='final1'),
    path('final2/', views.final2, name='final2'),
    path('final3/', views.final3, name='final3'),
    path('final4/', views.final4, name='final4'),
    path('outcome/<int:id>/', views.outcome, name='outcome'),
]
