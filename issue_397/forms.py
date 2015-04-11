# -*- encoding: utf-8 -*-
from django import forms
from . import models

import autocomplete_light
autocomplete_light.autodiscover()


class BookFormBase(autocomplete_light.ModelForm):

    class Meta:
        model = models.Book
        fields = ('authors', )


class BookForm(BookFormBase):
    # if model is NOT specified, then django-autocomplete-light 2.1.0RC2 doesn't work...
    '''class Meta:
        model = models.Book
        fields = ('authors', )
    '''
    pass


# pip install -e git+https://github.com/yourlabs/django-autocomplete-light.git#egg=autocomplete_light