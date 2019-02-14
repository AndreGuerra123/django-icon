from os import unlink
from PIL import Image
from django.test import TestCase
from .models import Icon, IconSmall
from django.core.exceptions import ValidationError


class IconTestCase(TestCase):
    def setUp(self):
        self.valid_icon_file = "test_resources/valid_icon.ico" 
        self.invalid_format_icon_file = "test_resources/invalid_icon.ico"
        self.valid_format_icon_file = "test_resources/valid_icon.png"

    def test_icon(self):
        """ Test simple icon creation """
        icon_object = Icon(ic=self.valid_icon_file)
        icon_object.full_clean()
    
    def test_format_fp_icon(self):
        """ Test simple icon creation (although having .ico prefix, its not a icon file)"""        
        icon_object= Icon(ic=self.invalid_format_icon_file)#Should throw
        self.assertRaises(ValidationError, icon_object.full_clean)

    def test_format_tn_icon(self):
        """ Test simple icon creation (although not having .ico prefix, its a icon file)"""        
        icon_object = Icon(ic=self.valid_format_icon_file)
        icon_object.full_clean()

    def test_dimensions(self):
        icon_object = IconSmall(ic=self.valid_icon_file)
        self.assertRaises(ValidationError, icon_object.full_clean)


    


    
        
    
        