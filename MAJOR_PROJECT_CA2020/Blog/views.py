from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blogpost
from django.urls import reverse_lazy

# Create your views here.
# def blogpost(request):
#    return render(request,'Blog/blogpost.html',{})

class HomeView(ListView):
    model = Blogpost
    template_name = 'Blog/blogpost.html'


class ArticleDetailView(DetailView):
    model = Blogpost
    template_name = 'Blog/blogdetail.html'


class AddPostView(CreateView):
    model = Blogpost
    template_name = 'Blog/addpost.html'
    fields = '__all__'


class UpdatedPostView(UpdateView):
    model = Blogpost
    template_name = 'Blog/updates_post.html'
    fields = '__all__'

class DeletePostView(DeleteView):
    model = Blogpost
    template_name = 'Blog/delete_post.html'
    success_url = reverse_lazy('home')