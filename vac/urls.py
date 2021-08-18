from django.urls import path

from vac.views import my_posts, search, main_page, create_post, post_delete, post_detail, category_posts

urlpatterns = [
    path('category/<int:pk>/', category_posts, name='category_details'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('post_delete/<int:pk>/', post_delete, name='post_delete'),
    path('my-posts/', my_posts, name='my_posts'),
    path('create-post/', create_post, name='create_job'),
    path('search/', search, name='search'),
    path('', main_page, name='main_page'),
    ]
