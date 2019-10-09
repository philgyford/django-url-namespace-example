from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the Books Index page.")


def detail(request, book_slug):
    return HttpResponse(
        'This is the Book Detail page (for a book with the slug "{}").'.format(
            book_slug
        )
    )
