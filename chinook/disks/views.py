from django.shortcuts import render

from .models import Album

def index(request):
    albums_list = Album.objects.order_by("title")
    context = {"albums_list": albums_list}
    return render(request, "disks/index.html", context)
