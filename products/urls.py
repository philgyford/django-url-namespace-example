from django.urls import include, path

from . import views
from books import urls as books_urls


app_name = "products"


urlpatterns = [
    path("", views.index, name="product_index"),

    path("books/", include(books_urls, namespace="books")),
]
