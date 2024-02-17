from django.urls import path
from . import views
urlpatterns = [
    
    path('login/', views.my_login, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.userlogout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('', views.homepage, name='home'),
    path('list_tasks/',views.list_tasks,name= 'list_tasks'),
    path('view_task/<int:task_id>/',views.view_task,name= 'view_task'),
    path('delete_task/<int:task_id>/',views.delete_task,name= 'delete_task'),
    path('update_task/<int:task_id>/',views.update_task,name= 'update_task'),
    path('create_task/',views.create_task,name= 'create_task'),
]