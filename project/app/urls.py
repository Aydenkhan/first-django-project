from django.urls import path
from . import views

urlpatterns = [
    path('abc', views.createe, name='list'),
    # path('register/', views.register, name='register'),

    path('register/', views.register, name= 'register'),
    path('delete/', views.delete, name='delete' ),
    path('update/<int:pk>',views.update, name='update'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
