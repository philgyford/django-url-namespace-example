# Django URL namespaces example

An example Django 2.2 project to demonstrate the use of nested URL namespaces, for
[this Stackoverflow question](https://stackoverflow.com/questions/12683494/defining-nested-namespaces-in-a-urlconf-for-reversing-django-urls-does-anyon/43459322).

This is a very simple project, with no models or admin, and extremely simple
views. It's purely for demonstrating how to nest URLs and their namespaces.

It includes the [django-extensions](https://django-extensions.readthedocs.io/en/latest/) module which isn't used in the code - it's purely so that if you want to view
the project's URLs you can do so by running its handy `show_urls` command:

```shell
$ ./manage.py show_urls
```

## Setup

Check out this repository and either use [pip](https://pip.pypa.io/en/stable/) to install the requirements:

```shell
$ pip install -r requirements.txt
```

Or use [pipenv](https://pipenv.readthedocs.io/en/latest/):

```shell
$ pipenv install
$ pipenv shell
```

Run Django's migrations (which will create the database file `db.sqlite3`):

```shell
$ ./manage.py migrate
```

Then you can start the Django development webserver:

```shell
$ ./manage.py runserver
```

You should be able to visit http://127.0.0.1:8000 in your browser.


## How it works

We have a Django project called `myproject` and two Django apps: `proudcts` and
`books`.

### `myproject/urls.py`

`myproject/urls.py` does two things:

1. Defines a URL for the home page (`""`).
2. Includes the `products/urls.py` file under the path `"products/"`

### `products/urls.py`

If we then look at the `products/urls.py` we can first see that it defines
an `app_name`. This is used when constructing the URL names for the URLs it
defines and includes.

It then does two things:

1. Defines a URL for the produts index page (`""`).
2. Includes the `books/urls.py` file under the path `"books/"`.

Note that because this was included under the path `"products/"`, this is
added to the start of the two URLs it defines.

So the products index page `""` will be `"products/"`.  
And the books URLs will be under `"products/books/"`.

### `books/urls.py`

If we then look at the `books/urls.py` we can first see that it defines an
`app_name` which, as before, is used when constructing the URL names for the
URLs it defines and includes.

It then also does two things:

1. Defines a URL for the books index page (`""`).
2. Defines a URL for a book, identified by a slug (`"<slug:book_slug>/"`).

Note that because this was included under the path `"books/"`, from
`products.urls`, which in turn was included under the path `"products/"`, these
are both added to the start of the two URLs it defines.

So the books index page `""` will be `"products/books/"`.  
And the book detail URL will be like `"products/books/<slug>/"`.

### Putting it together

The result is that we have defined the following URLs, each linked to a view,
and each identified by a specific URL name. If you're running the site with
the Django development webserver (see above) then the links below should work:

| URL                           | View                 | Name                         |
| ----------------------------- | -------------------- | ---------------------------- |
| [`/`][1]                      | `products.site_home` | `home`                       |
| [`/products/`][2]             | `products.index`     | `products:product_index`     |
| [`/products/books/`][3]       | `books.index`        | `products:books:book_index`  |
| [`/products/books/<slug>`][4] | `books.views.detail` | `products:books:book_detail` |

[1]: http://127.0.0.1:8000
[2]: http://127.0.0.1:8000/products/
[3]: http://127.0.0.1:8000/products/books/
[4]: http://127.0.0.1:8000/products/books/an-example-book/


## About

Home: https://github.com/philgyford/django-url-namespace-example  
By: Phil Gyford (phil@gyford.com)
