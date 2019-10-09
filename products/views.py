from django.http import HttpResponse


def site_home(request):
    return HttpResponse("This is the main home page of the site.")


def index(request):
    return HttpResponse("This is the Products Index page.")
