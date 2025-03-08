from django.db import models

# Create your models here.
class Qrcode(models.Model):
    
    shape_choises = [
        ('square', 'Square'), 
        ('circle', 'Circle')
    ]
    
    pattern_choises = [
        ('dots', 'Dots'),
        ('lines', 'Lines'),
        ('square', 'Square'),
    ]
    
    name = models.CharField(max_length= 250)
    link = models.URLField()
    shape = models.CharField(max_length = 250, default = 'square', choices = shape_choises)
    patern = models.CharField(max_length = 250, default = 'regular', choices = pattern_choises)
    bg_color = models.CharField(max_length = 250, default = '#000000')
    fg_color = models.CharField(max_length = 250, default = '#000000')
    gradient = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'qr_iamges/', blank = True, null = True)
    time = models.DateTimeField(auto_now_add = True)