from .models import *

class DataMixin:
    paginate_by = 20
    model = Spravochnik
    context_object_name = 'items'
    allow_empty = False