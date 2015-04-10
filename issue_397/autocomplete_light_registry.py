# -*- encoding: utf-8 -*-

import autocomplete_light
from .models import Author


autocomplete_light.register(Author,
    search_fields=['name'],
    attrs={
        'placeholder': 'Search for author...',
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 5,
        'class': 'modern-style',
    },
)