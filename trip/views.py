from django.shortcuts import render
from .models import *
from place.models import Season, City, TypePlace
from django.views import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from travel import settings
from slugify import slugify
import os


def index(request):
    trips = Trip.objects.all()
    seasons = Season.objects.all()
    cities = City.objects.all()
    type_places = TypePlace.objects.all()
    return render(request, 'trip/index.html', locals())


def page_of_trip(request, id):
    # title = 'Страница тура'
    trip = Trip.objects.get(id=id)
    title = trip.title
    return render(request, 'trip/page_of_trip.html', locals())


class ChangeFavouriteTrip(View):
    def get(self, request, id):
        kwargs = {}
        try:
            trip = Trip.objects.get(id=id)
            favourite = FavouriteTrip.objects.filter(trip=trip)
            if favourite.exists():
                favourite.delete()
                type = 'deactivate'
            else:
                FavouriteTrip.objects.create(trip=trip, user=request.user)
                type = 'active'
            kwargs['type'] = type
            kwargs['status'] = 1
        except Exception:
            kwargs['status'] = 0
        return JsonResponse({**kwargs})


def pdf_trip(request, id):
    places = UserPlace.objects.filter(trip_id=id).order_by('visit_date', 'visit_time')
    return render(request, 'trip/pdf.html', locals())


def html_to_pdf(request, id):
    import pdfkit
    try:
        config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
        pdfkit.from_url(f'http://127.0.0.1:8000/trip/pdf/{id}', os.path.abspath('trip.pdf'), configuration=config)
    except:
        pdfkit.from_url(f'http://127.0.0.1:8000/trip/pdf/{id}', os.path.abspath('trip.pdf'))
    trip = UserTrip.objects.get(id=id)
    test_file = open(os.path.abspath('trip.pdf'), 'rb')
    response = HttpResponse(content=test_file)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'attachment; filename="{slugify(trip.title)}.pdf"'
    return response
