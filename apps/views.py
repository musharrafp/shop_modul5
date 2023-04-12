from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from apps.models import Product, Blog


# class Blog_View(TemplateView):
#     template_name = 'blog/blog-list.html'
#
#
# class BlogDetel_View(DetailView):
#     template_name = 'blog/blog-details.html'


class Post_View(ListView):
    model = Product
    template_name = 'product/shop-left-sidebar.html'


class PostDetel_View(DetailView):
    model = Product
    template_name = 'product/single-product.html'


class Blog_View(ListView):
    model = Blog
    template_name = 'blog/blog-list.html'


class BlogDetel_View(DetailView):
    model = Blog
    template_name = 'blog/blog-details.html'


class AddBlog(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blog')
    template_name = 'addblog.html'
