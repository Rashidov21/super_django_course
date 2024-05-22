from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Category,Movie

class MovieListView(ListView):
    model = Movie
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    

class MovieDetailView(DetailView):
    model = Movie
    template_name = "film.html"\


class MovieCategoryListView(ListView):
    model = Movie
    template_name = "films.html"
    
    
    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        category = Category.objects.get(slug=category_slug)
        return Movie.objects.filter(category=category)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("slug")
        category_slug = self.kwargs.get("slug")
        category = Category.objects.get(slug=category_slug)
        
        context["category"] = category
        context["categories"] = Category.objects.all()
        return context
    
    