
from django.urls import path
from .view import *
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('about/', about_page),
    path('post/', post_page),
    path('post/post_1/', post1_page, name='post_1'),
    path('post/post_2/', post2_page, name='post_2'),
    path('post/post_3/', post3_page, name='post_3'),
    path('otzivi/', otziv_page, name='otziv_page'),
    path('image/logo/', logo_image, name='logo_image'),
    
]
