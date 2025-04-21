from django import forms
from .models import Qrcode


class QRCodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        # fields = ['name', 'link', 'bg_color', 'fg_color', 'patterns', 'border_width', 'image']
        fields = '__all__'
       
        widgets = {
            'name': forms.TextInput(
                attrs= {
                'class': 'form-name',
                'id': 'name'
            }),
           
            'link': forms.URLInput(
                attrs= {
                'class': 'form-url',
                'id': 'link'
            }),
           
           'bg_color': forms.TextInput(
                attrs= {
                    'type': 'color', 
                    'class': 'bg-color',
                    'value': '#4f4949',
                    'id': 'bg_color'
                }
           ),
           
           'fg_color': forms.TextInput(
                attrs= {
                   'type': 'color', 
                   'class': 'fg-color',
                   'value': '#4f4949',
                    'id': 'fg_color'
                }
           ),
           
           'patterns': forms.Select(
                attrs= {
                'class': 'form-pattern',
                    'id': 'patterns'
            }
           ),
           
           'border_width': forms.NumberInput(
               attrs= {
                'class': 'qr-width', 
                'min': 1,
                'id': 'border_width'
            }
           ),
           
           "image": forms.ClearableFileInput(
               attrs= {
                'class': 'qr-img',
                'id': 'image'
            }
           )
       }


        #    'border': forms.Select(
        #        attrs= {
        #         'class': 'qr-border',
        #             'id': 'border'
        #     }
        #    ),
        
    
           