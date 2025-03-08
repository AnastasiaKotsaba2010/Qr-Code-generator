from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length= 250,
        widget= forms.TextInput( attrs= {
            'class': 'input-text',
        })
    )
    email = forms.EmailField(
        widget= forms.EmailInput(attrs= {
            'class': 'input-text',
        })
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs= {
            'class': 'input-text'
        })
    )
