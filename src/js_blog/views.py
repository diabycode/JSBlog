from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenu dans le blog de JOJO !")


