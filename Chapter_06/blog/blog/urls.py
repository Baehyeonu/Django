from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render
from member import views as member_views
from django.views.generic import TemplateView, RedirectView
from django.views import View

from blog import views
from blog import cb_viesw

app_name = 'blog'

urlpatterns = [
        #CBV blog
    path('', cb_viesw.BloglistView.as_view(), name='list'),
    path('<int:blog_pk>/', cb_viesw.BlogDetailView.as_view(), name = 'detail'),
    path('create/', cb_viesw.BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update/', cb_viesw.BlogUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', cb_viesw.BlogDeleteView.as_view(), name = 'delete'),
    path('comment/create/<int:blog_pk>', cb_viesw.CommentCreateView.as_view(), name='comment_create')
]