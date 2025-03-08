from django import forms
from .models import Qrcode


class QRCodeForm(forms.ModelForm):
    class Meta:
       model = Qrcode
       fields = '__all__'
       widget = {
           'bg_color': forms.TextInput(
               attrs= {'type': 'color'}
           ),
           
           'fg_color': forms.TextInput(
               attrs= {'type': 'color'}
           )
       }
    
    
    
    
    
    
    
    
    
    
    
    
    
#     name = forms.CharField(label = "Name:", required = True)
#     url = forms.URLField(label = "URL:", required = True, max_length = 100)
#     #                                                                                       <input type="color">
#     qr_color = forms.CharField(label = "Foreground color:", widget = forms.TextInput(attrs= {'type': "color"}), initial= '#000000')
#     bg_color = forms.CharField(label = "Background color:", widget = forms.TextInput(attrs= {'type': "color"}), initial= '#FFFFFF')
    
#     border = forms.IntegerField(label = 'Border width:', min_value = 1, max_value = 10)
#     border_radius = forms.BooleanField(label = 'Border radius:', required = False)
#     logo_image = forms.ImageField(label = 'Logo image (optional):', required = False)

