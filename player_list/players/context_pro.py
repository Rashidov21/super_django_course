from .models import Tournament,Club

POS = (
    ("gk","GoalKeeper"),
    ("df","Deffender"),
    ("mdf","Middle deffender"),
    ("fw","Forward"),
    ("st","Striker")
)


def get_all(request):
    if "filter" in request.path: 
        tournaments = Tournament.objects.all()
        clubs = Club.objects.all()
        context = {
            "tournaments":tournaments,
            "clubs":clubs,
            "positions":POS
        }
        return context