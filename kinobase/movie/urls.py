from django.urls import path
from . import views

app_name = "movie"


urlpatterns = [
    path("",views.MovieListView.as_view(), name="movie_list"),
    path("film/<slug>", views.MovieDetailView.as_view(), name="movie_detail"),
    path("category/<slug>", views.MovieCategoryListView.as_view(), name="movie_category_list"),
    
    # FILTER AND SORTING 
    path("filter/<filter_by_what>/<filter_by>", views.MovieFilterView.as_view(), name="movie_filter")
]
