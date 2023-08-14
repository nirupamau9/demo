
from django.http import HttpResponse
from django.shortcuts import render

from demotravelapp.models import Place, Team


# Create your views here.
def demo(request):
    places = Place.objects.all()
    teams = Team.objects.all()
    places_data = [{'name': place.name, 'img_url': place.img.url, 'desc': place.desc} for place in places]
    teams_data = [{'name1': team.name1, 'img1_url': team.img1.url, 'desc1': team.desc1} for team in teams]
    return render(request, "index.html", {'places_data': places_data, 'teams_data': teams_data})

