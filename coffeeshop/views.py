from django.shortcuts import render
from coffee.models import contactt_us, Coffee, Reservation

def Master(request):

    return render(request, 'master.html')


def Home(request):

    return render(request, 'home.html')



def Contact_us(request):
    if request.method == "POST":
        contact = contactt_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request, 'contact_us.html')


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')

def Menu(request):

    coffee = Coffee.objects.all()
    context = {
        'coffee': coffee
    }
    return render(request, 'menu.html', context)

def Reserve(request):
    if request.method == "POST":
        reserve = Reservation(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            date = request.POST.get('date'),
            time = request.POST.get('time')
        )
        reserve.save()


    return render(request, 'reservation.html')