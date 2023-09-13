
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Players
from .forms import AdPlayerForm

# Create your views here.


class PlayerListView(ListView):
    model = Players
    template_name = 'home.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        # return qs.filter(role="вратарь")
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["test_obj"] = Players.objects.get() # 1 obj  (fetchone)
        # context["test_obj"] = Players.objects.get_or_create() # 1 obj if not, create
        # context["test_obj"] = Players.objects.all() # all objects
        # context["test_obj"] = Players.objects.filter() # filtering objects
        # context["test_obj"] = Players.objects.exclude() # exclude and filtering objects
        # context["test_obj"] = Players.objects.in_bulk() # group objects create
        # get 
        # context['test_obj'] = Players.objects.get(role="защитник",age=25)
        # get_or_create 
        # context['test_obj'] = Players.objects.get_or_create(player="Матей Коварж",dr='2000-05-17' ,age=23)
        # all 
        # context["test_obj"] = Players.objects.all() # all objects
        # filter 
        # context["test_obj"] = Players.objects.filter(age__lte=25) # all objects
        # exclude 
        # context["test_obj"] = Players.objects.exclude(role="защитник") # all objects
        # print(type(context["test_obj"]))
        # in_bulk
        # context["test_obj"] = Players.objects.in_bulk() # dict objects
        return context

class PlayerAdView(CreateView):
    model = Players
    form_class = AdPlayerForm 
    # template_name = ''
    success_url = '/'