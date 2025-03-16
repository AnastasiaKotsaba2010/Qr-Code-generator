from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User

# Create your models here.
class Qrcode(models.Model):
    
    border_choises = [
        ('square', 'Square'), 
        ('circle', 'Circle')
    ]
    
    pattern_choises = [
        ('dots', 'Dots'),
        ('lines', 'Lines'),
        ('square', 'Square'),
    ]
    
    user = models.ForeignKey(to = User, on_delete= models.CASCADE, default= None)
    
    name = models.CharField(max_length= 250)
    link = models.URLField()
    border = models.CharField(max_length = 250, default = 'square', choices = border_choises)
    border_width = models.IntegerField(default= 4)
    patterns = models.CharField(max_length = 250, default = 'square', choices = pattern_choises)
    bg_color = models.CharField(max_length = 250, default = '')
    # bg_color = ColorField(default= '#000000')
    fg_color = models.CharField(max_length = 250, default = '')
    # fg_color = ColorField()
    gradient = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'qr_codes/', blank = True, null = True)
    time = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    