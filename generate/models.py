from django.db import models

# Create your models here.
class Qrcode(models.Model):    
    pattern_choises = [
        ('dots', 'Dots'),
        ('lines', 'Lines'),
        ('square', 'Square'),
    ]
    
    name = models.CharField(max_length= 250)
    link = models.URLField()
    
    border_width = models.IntegerField(default= 4)
    
    patterns = models.CharField(max_length = 250, default = 'square', choices = pattern_choises)
    bg_color = models.CharField(max_length = 250, default = '')
    fg_color = models.CharField(max_length = 250, default = '')
    image = models.ImageField(blank = True, null = True)
    
    def __str__(self):
        return self.name
    
# border = models.CharField(max_length = 250, default = 'square', choices = border_choises)
# time = models.DateTimeField(auto_now_add = True)
# gradient = models.BooleanField(default = False)