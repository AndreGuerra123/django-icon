from django.db import models
from .fields import IconField
class Icon(models.Model):
    ic = IconField()

class IconSmall(models.Model):
    ic = IconField(min_height=10,max_height=10,min_width=10,max_width=10)
