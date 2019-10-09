from django.urls import path

from . import views


app_name = "books"


urlpatterns = [
    path("", views.index, name="book_index"),

    path("<slug:book_slug>/", views.detail, name="book_detail"),
]
