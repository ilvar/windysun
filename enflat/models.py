from django.db import models
from django.contrib.flatpages.models import FlatPage

from meta.models import MetaModel

class CustomFlatPage(FlatPage, MetaModel):
    pass
