from django.urls import path
from . import views

urlpatterns = [
    #auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
#projects
    path('', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
#attachments
    path('projects/<int:pk>/attachments/create/', views.attachment_create, name='attachment_create'),
    path('attachments/<int:pk>/delete/', views.attachment_destroy, name='attachment_destroy'),
#threads
    path('projects/<int:pk>/threads/create/', views.thread_create, name='thread_create'),
    path('threads/<int:pk>/edit/', views.thread_edit, name='thread_edit'),
    path('threads/<int:pk>/delete/', views.thread_destroy, name='thread_destroy'),
#messages
    path('threads/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:pk>/messages/create/', views.message_create, name='message_create'),
    path('messages/<int:pk>/edit/', views.message_edit, name='message_edit'),
    path('messages/<int:pk>/delete/', views.message_destroy, name='message_destroy'),
]