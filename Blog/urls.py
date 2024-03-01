from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/post', views.dashboard_post, name='dashboard_post'),
    path('dashboard/post/new', views.dashboard_posts_new, name='dashboard_posts_new'),
    path('dashboard/post/view/<str:slug>', views.dashboard_posts_view, name='dashboard_posts_view'),
    path('dashboard/post/edit/<str:slug>', views.dashboard_posts_edit, name='dashboard_posts_edit'),
    path('dashboard/post/delete/<str:slug>', views.dashboard_post_delete, name='dashboard_post_delete'),
    path('post/<str:slug>/', views.single_post, name='single_post')
]

