from django.views import generic
from . import forms
from . import models


class CreateBookView(generic.CreateView):

    model = models.Book
    form_class = forms.BookForm
    template_name = "book_create.html"
