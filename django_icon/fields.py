
from django.db import models
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from django.core import checks
from django.conf import settings
import intervals as I
from .validators import validate_icon

default_min = getattr(settings,'ICON_MIN',16)
default_max = getattr(settings,'ICON_MAX',256)

class IconField(models.ImageField):
    '''Icon model field based on a Django ImageField''' 
    description = _('Icon image.')

    def validate(self,value, model_instance):
        validate_icon(value, self.min_width,self.max_width,self.min_height,self.max_height)
        super(IconField,self).validate(value, model_instance)
        
    def __init__(self,
        min_width:int=default_min,
        min_height:int=default_min,
        max_width:int=default_max,
        max_height:int=default_max,
        **kwargs): 

        self.min_width = min_width
        self.min_height = min_height
        self.max_width = max_width
        self.max_height = max_height

        super().__init__(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        if self.min_width != default_min:
            kwargs['min_width']= self.min_width
        if self.max_width != default_max:
            kwargs['max_width']= self.max_width
        if self.min_height != default_min:
            kwargs['min_height']= self.min_height
        if self.max_height != default_max:
            kwargs['max_height']= self.max_height

        return name, path, args, kwargs

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_kwargs()
        ]

    def _check_kwargs(self):
    
        if I.closed(self.min_width,self.max_width).is_empty():    
                return [
                        checks.Error(
                            "%s's width range is empty. Check min_width and max_width parameters." % self.__class__.__name__,
                            obj=self,
                            id='fields.E001',
                        )
                    ]

        if I.closed(self.min_height,self.max_height).is_empty():    
                return [
                        checks.Error(
                            "%s's height range is empty. Check min_height and max_height parameters." % self.__class__.__name__,
                            obj=self,
                            id='fields.E001',
                        )
                    ]              

        return []

    