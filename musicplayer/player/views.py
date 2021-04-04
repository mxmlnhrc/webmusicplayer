from django.shortcuts import render

from .models import Song


# Create your views here.
def index(request):
    latest = Song.objects.all().order_by('-id')[:5]
    return render(request, "player/index.html", {
        'latest': latest,
    })