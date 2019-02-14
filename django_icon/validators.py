import os
from PIL import Image
import intervals as I
from django.core.exceptions import ValidationError

def validate_icon(value,min_w:(int,None),max_w:(int,None),min_h:(int,None),max_h:(int,None)):
    try:
        img = Image.open(value)    
        w, h = img.size
    except Exception as e:
        raise ValidationError(e)

    p_min_w = min_w if min_w else -I.inf
    p_max_w = max_w if min_w else I.inf
    p_min_h = min_h if min_h else -I.inf
    p_max_h = max_h if min_h else I.inf

    w_range = I.closed(p_min_w,p_max_w)
    h_range = I.closed(p_min_h,p_max_h)

    if img.format != 'ICO':
        raise ValidationError('Unsupported file type, only icon image files (.ico) are accepted.')

    if not w_range.contains(w):
        raise ValidationError('Unsupported icon dimensons: only icons with a width of  %s px are accepted.'%(str(w_range)))
    
    if not h_range.contains(h):
        raise ValidationError('Unsupported icon dimensons: only icons with a height of  %s px are accepted.'%(str(h_range)))

