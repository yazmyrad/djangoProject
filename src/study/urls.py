from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_blog/', views.create_blog, name='blog_creation'),
    path('<slug:slug>/', views.blog, name="blog_detail"),
    path('tag/<slug:tag_slug>', views.home, name="blog_tag")
]

handler404 = "study.views.pageNotFound"