import qrcode
from django.shortcuts import render, redirect
from django.http import HttpRequest
import qrcode.constants
from .forms import QRCodeForm

# Create your views here.
def render_generate(request: HttpRequest):
    form = QRCodeForm()
    if request.method == "POST":
        form = QRCodeForm(request.POST, request.FILES)
        
        if form.is_valid():
            # name = form.cleaned_data.get('name')
            # url = form.cleaned_data.get('url')
            # qr_color = form.cleaned_data.get('qr_color')
            # bg_color = form.cleaned_data.get('bg_color')
            # border = form.cleaned_data.get('border')
            # border_radius = form.cleaned_data.get('border_radius')
            # logo_image = form.cleaned_data.get('logo_image')
            
            # qr = qrcode.QRCode(
            #     version = 3,
            #     error_correction = qrcode.constants.ERROR_CORRECT_H, 
            #     box_size = 5,
            #     border = border
            # )
            
            # qr.add_data(url)
            # qr.make(fit= True)
            
            form.save()
            return redirect('/')
    else:
        form = QRCodeForm(request.POST, request.FILES)
            # print(f'name: {name}, url: {url}, qr_color{qr_color}, bg_color: {bg_color}, border:{border}, border_radius: {border_radius}, logo_image: {logo_image} ')
    
    return render(request = request, template_name = 'generate_page/generate.html', context= {'form': form})