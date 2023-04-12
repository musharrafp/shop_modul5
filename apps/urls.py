from django.urls import path
from apps.views import Post_View, PostDetel_View,Blog_View,BlogDetel_View,AddBlog

urlpatterns = [
    path('', Blog_View.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetel_View.as_view(), name='blog_view'),
    path('p', Post_View.as_view(), name='post'),
    path('post/<int:pk>', PostDetel_View.as_view(), name='post_view'),
    path('add',AddBlog.as_view(), name='add'),
]
