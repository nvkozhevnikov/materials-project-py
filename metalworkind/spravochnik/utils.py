from .models import *

class DataMixin:
    paginate_by = 20
    model = Spravochnik
    allow_empty = False
    context_object_name = 'items'