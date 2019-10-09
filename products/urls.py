from django.urls import include, path

from books import urls as books_urls
from . import views


app_name = "products"


urlpatterns = [
    path("", views.index, name="product_index"),

    path("books/", include(books_urls, namespace="books")),
]
