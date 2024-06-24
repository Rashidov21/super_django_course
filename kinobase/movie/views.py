from typing import Any
import datetime
from datetime import timedelta
from django.db.models.query import QuerySet
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Category,Movie,Genre,Comment
from users.forms import SetCommentForm


class MovieListView(ListView):
    model = Movie
    template_name = "index.html"
    
    def get_queryset(self):
        qs = Movie.objects.filter(drafts=False)
        print(dir(Movie))
        return qs
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    

class MovieDetailView(DetailView):
    model = Movie
    template_name = "film.html"
    
    def get_queryset(self):
        return (
            Movie.objects
            .select_related("category")  # Categorical ma'lumotlarni birgalikda olish
            .prefetch_related("genres")  # Genre ma'lumotlarini oldindan yuklash
            .filter(slug=self.kwargs.get("slug"), drafts=False)  # Filtrlashni to'g'ri qo'llash
            )

    # def get_object(self):
    #     return get_object_or_404(self.get_queryset(), slug=self.kwargs.get('slug'))
    
    
    def get_context_data(self, **kwargs):
        form = SetCommentForm()
        if self.request.user.is_authenticated:
            if self.object.id not in self.request.user.profile.history.all():
                self.request.user.profile.history.add(self.object.id )
            else:
                pass
        if self.request.method == "POST":
            print("OK")
        context = super().get_context_data(**kwargs)
        context["form"] = form
        context["comments"] = Comment.objects.filter(movie=self.object).select_related("movie")
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = SetCommentForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        self.object = self.get_object()
        comment = form.cleaned_data['comment']
        if len(comment) > 2:
            if self.request.user.is_authenticated:
                Comment.objects.create(
                author=self.request.user.first_name,
                comment=comment,
                movie=self.object)
                messages.success(self.request,"Comment added !")
            else:
                messages.success(self.request,"Пользователь не может комментировать. Если у вас возникли вопросы, напишите письмо на электронную почту support@kinobase.org")
             
        return HttpResponseRedirect(reverse('movie:movie_detail', args=[str(self.object.slug)]))

class MovieCategoryListView(ListView):
    model = Movie
    template_name = "films.html"
    paginate_by = 5
    
    
    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        category = Category.objects.get(slug=category_slug)
        return Movie.objects.select_related("category").prefetch_related("genres").filter(category=category)


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
            qs = Movie.objects.filter(country=self.kwargs.get("filter_by"))
            return qs
        if self.kwargs.get("filter_by_what") == "year":
            qs = Movie.objects.filter(year=self.kwargs.get("filter_by"))
            return qs
        if self.kwargs.get("filter_by_what") == "quality":
            qs = Movie.objects.filter(quality__icontains=self.kwargs.get("filter_by"))
            return qs
        
_now = datetime.datetime.now()     
class MovieSortView(ListView):
    model = Movie
    template_name = "films.html"
    paginate_by = 3
    
    def get_queryset(self):
        if self.kwargs.get("sort_by") == "new":
            qs = Movie.objects.all().order_by("-id")
            return qs
        if self.kwargs.get("sort_by") == "year":
            qs = sorted(Movie.objects.filter(ratings__created_at__year=_now.year),key=lambda m: m.get_average_rating(), reverse=True)
            return list(set(qs))
        if self.kwargs.get("sort_by") == "day":
            qs = sorted(Movie.objects.filter(ratings__created_at__day=_now.day),key=lambda m: m.get_average_rating(), reverse=True)
            return list(set(qs))
        if self.kwargs.get("sort_by") == "week":
            last_week = _now - timedelta(days=7)
            qs = sorted(Movie.objects.filter(ratings__created_at__range=[last_week, _now]),key=lambda m: m.get_average_rating(), reverse=True)
            return list(set(qs))
        if self.kwargs.get("sort_by") == "month":
            last_month = _now - timedelta(days=30)
            qs = sorted(Movie.objects.filter(ratings__created_at__range=[last_month, _now]),key=lambda m: m.get_average_rating(), reverse=True)
            return list(set(qs))
        if self.kwargs.get("sort_by") == "alltime":
            qs = sorted(Movie.objects.all(),key=lambda m: m.get_average_rating(), reverse=True)
            return qs
        if self.kwargs.get("sort_by") == "kp_rating":
            qs = sorted(Movie.objects.all(),key=lambda m: m.kp_rating, reverse=True)
            return qs
        if self.kwargs.get("sort_by") == "imdb_rating":
            qs = sorted(Movie.objects.all(),key=lambda m: m.imdb_rating, reverse=True)
            return qs
        if self.kwargs.get("sort_by") == "users_rating":
            qs = sorted(Movie.objects.all(),key=lambda m: m.get_average_rating(), reverse=True)
            return qs


def search(request):
    query = request.GET.get("data")
    object_list = Movie.objects.filter(
        Q(title__icontains=query) | Q(origin_title__icontains=query)
    )
    if object_list:
        print(len(object_list))
    return JsonResponse({"data":list(object_list.values())})


def comment_delete(request, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))