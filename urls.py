from django.urls import path

from S import views

urlpatterns = [
    path('', views.login_fun, name='log'),
    path('signup/', views.signup_fun, name='signup'),
    path('home/', views.home_fun, name='home'),
    path('add/', views.addstudents, name='add'),
    path('display/', views.displaystudents, name='display'),
    path('update/<int:id>',views.update_students,name='update'),
    path('delete/<int:id>', views.delete_students, name='delete'),
]
