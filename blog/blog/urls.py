"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .view import *

urlpatterns = [
    path('', index_page),
    path('about/', about_page),
    path('post/', post_page),
    path('post/post_1/', post1_page, name='post_1'),
    path('post/post_2/', post2_page, name='post_2'),
    path('post/post_3/', post3_page, name='post_3'),
    path('image/logo/', logo_image, name='logo_image'),
    
]
