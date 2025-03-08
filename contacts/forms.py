from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 250)
    last_name = forms.CharField(max_length = 250)
    email = forms.EmailField(required= False, max_length = 250)
    # phone = forms.(max_length =)
    
    