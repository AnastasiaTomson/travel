from django.shortcuts import render
from trip.models import *
from place.models import *
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.core import mail
from travel import settings


def front(request):
    places = Place.objects.filter(image__isnull=False).distinct().order_by("?")[:8]
    trips = Trip.objects.all().order_by("?")[:3]
    images = Image.objects.all().order_by("?")[:8]
    return render(request, 'front/index.html', locals())


@require_http_methods(["POST"])
def feedback(request):
    if request.method == 'POST':
        if request.POST.get('email') != '' and \
                request.POST.get('name') != '' and \
                request.POST.get('phone') != '':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            message = f"Есть вопросы\n Имя: {name}\nТелефон: {phone}\nПочта: {email}"
            recipients = ['office_windtravel@mail.ru']
            msg = mail.EmailMessage(f'Появились вопросы у {name}', message, settings.EMAIL_HOST_USER, recipients)
            msg.send()
    return redirect('front')
