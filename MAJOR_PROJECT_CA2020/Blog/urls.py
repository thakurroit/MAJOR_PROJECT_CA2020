from django.urls import path,include
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatedPostView, DeletePostView
urlpatterns = [

#    path('blogpost/',views.blogpost, name='blogHome'),
    path('blogpost/',HomeView.as_view(),name='home'),
    path('blogdetail/<int:pk>',ArticleDetailView.as_view(),name='details'),
    path('blogdetail/edit/<int:pk>',UpdatedPostView.as_view(),name='updates_post'),
    path('blogdetail/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    path('addpost/', AddPostView.as_view(), name='addpost'),

    ]