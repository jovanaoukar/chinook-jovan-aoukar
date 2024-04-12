from django.shortcuts import get_object_or_404, render

from .models import Album

def index(request):
    albums_list = Album.objects.order_by("title")
    context = {"albums_list": albums_list}
    return render(request, "disks/index.html", context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {"album": album}
    return render(request, "disks/detail.html", context)