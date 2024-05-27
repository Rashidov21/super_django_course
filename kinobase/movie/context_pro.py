from .models import Category,Genre,Movie

def get_movie_countries():
    countr_list = []
    for movie in Movie.objects.all():
        for country in movie.country:
            countr_list.append({"name":country.name,"code":country.code})
    # return set([{"name":i.name,"code":i.code} for x in Movie.objects.all() for i in x.country])
    return countr_list
    
    


def get_context(request):
    context = {
        "genres":Genre.objects.all(),
        "movie_countries":get_movie_countries()
    }
    return context