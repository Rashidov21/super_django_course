from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Category,Movie,Genre

class MovieListView(ListView):
    model = Movie
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    

class MovieDetailView(DetailView):
    model = Movie
    template_name = "film.html"


class MovieCategoryListView(ListView):
    model = Movie
    template_name = "films.html"
    paginate_by = 1
    
    
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
    
class MovieFilterView(ListView):
    model = Movie
    template_name = "films.html"
    paginate_by = 5
    
    def get_queryset(self):
        if self.kwargs.get("filter_by_what") == "genre":
            genre = Genre.objects.get(slug=self.kwargs.get("filter_by"))
            qs = Movie.objects.filter(genres=genre)
            return qs
        if self.kwargs.get("filter_by_what") == "country":
            print(self.kwargs.get("filter_by"))
            qs = Movie.objects.filter(country=self.kwargs.get("filter_by"))
            return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context