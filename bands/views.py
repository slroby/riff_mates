from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from bands.models import Musician
from bands.models import Band


def musician(request, musician_id):

    musician = get_object_or_404(Musician, id=musician_id)

    data = {"musician": musician}

    return render(request, "musician.html", data)


def musicians(request):

    print(request.GET)

    all_musicians = Musician.objects.all().order_by("last_name")

    num_objects = request.GET.get("num", 2)

    if int(num_objects) > 10:
        num_objects = 10

    paginator = Paginator(all_musicians, num_objects)

    page_num = request.GET.get("page", 1)
    page_num = int(page_num)

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)

    data = {
        "musicians": page.object_list,
        "page": page,
    }

    return render(request, "musicians.html", data)


def band(request, band_id):

    band = get_object_or_404(Band, id=band_id)
    print(band)

    data = {
        "band": band,
    }

    return render(request, "band.html", data)


def bands(request):

    print(request.GET)

    all_bands = Band.objects.all().order_by("name")

    num_objects = request.GET.get("num", 2)

    if int(num_objects) > 10:
        num_objects = 10

    paginator = Paginator(all_bands, num_objects)

    page_num = request.GET.get("page", 1)
    page_num = int(page_num)

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)

    data = {
        "bands": page.object_list,
        "page": page,
    }

    return render(request, "bands.html", data)


print("http://127.0.0.1:8000/bands/musician/1")
print("http://127.0.0.1:8000/bands/musicians/")
print("http://127.0.0.1:8000/bands/band/1")
print("http://127.0.0.1:8000/bands/bands/")
