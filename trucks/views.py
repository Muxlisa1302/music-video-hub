from django.shortcuts import render, redirect, get_object_or_404
from .models import Truck


def home(request):
    return render(request, 'index.html')


def truck_list(request):
    trucks = Truck.objects.all()
    ctx = {'trucks': trucks}
    return render(request, 'trucks/music-list.html', ctx)


def truck_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        image = request.FILES.get('image')
        audio = request.FILES.get('audio')
        if title and artist and album and genre and image and audio:
            Truck.objects.create(
                title=title,
                artist=artist,
                album=album,
                genre=genre,
                image=image,
                audio=audio,
            )
            return redirect('trucks:list')
    return render(request, 'trucks/music-create.html')



def truck_detail(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    ctx = {'truck': truck }
    return render(request, 'trucks/music-detail.html', ctx)

def truck_delete(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    truck.delete()
    return redirect('trucks:list')

def truck_update(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        image = request.FILES.get('image')
        audio = request.FILES.get('audio')
        if title and artist and album and genre and image and audio:
            truck.title=title,
            truck.artist=artist,
            truck.album=album,
            truck.genre=genre,
            truck.image=image,
            truck.audio=audio,
            truck.save()
            return redirect('trucks:detail')


def video_list(request):
    return render(request, 'video-list.html')
