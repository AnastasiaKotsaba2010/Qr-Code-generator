from django.shortcuts import render, redirect
from django.http import HttpRequest
import qrcode, os
from PIL import Image
from .forms import QRCodeForm
from .models import Qrcode
from QrCode import settings

def generate_qr(request: HttpRequest):
    form = QRCodeForm()
    
    if request.method == 'POST':
        qr_form = QRCodeForm(request.POST, request.FILES)

        if qr_form.is_valid():
            name = qr_form.cleaned_data.get('name')
            link = qr_form.cleaned_data.get('link')
            border_width = qr_form.cleaned_data.get('border_width')
            patterns = qr_form.cleaned_data.get('patterns')
            bg_color = qr_form.cleaned_data.get('bg_color')
            fg_color = qr_form.cleaned_data.get('fg_color')
            img = qr_form.cleaned_data.get('image')

            qr = qrcode.QRCode(
                version= 1,
                error_correction= qrcode.constants.ERROR_CORRECT_H,
                box_size= 10,
                border= border_width
            )
            
            qr.add_data(link)
            qr.make(fit=True)

            qr_img = qr.make_image(
                fill_color=fg_color, 
                back_color=bg_color
            ).convert("RGBA")

            if img:
                logo = Image.open(img)
                base_width = 75
                
                w_percent = base_width / float(logo.size[0])
                h_size = int((float(logo.size[1]) * float(w_percent)))
                resized_logo = logo.resize((base_width, h_size), Image.Resampling.LANCZOS)

                position = (
                    (qr_img.size[0] - resized_logo.size[0]) // 2,
                    (qr_img.size[1] - resized_logo.size[1]) // 2
                )
                qr_img.paste(resized_logo, position, mask=resized_logo.convert("RGBA"))


            file_name = f'{name}.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr_img.save(file_path)

            qr_image_url = os.path.join(settings.MEDIA_URL, file_name) 
            
            qr_instance = Qrcode(
                name= name,
                link= link,
                bg_color= bg_color,
                fg_color= fg_color,
                border_width= border_width,
                patterns= patterns    
            )
            
            qr_instance.save()
           
            return render(
                request,
                'generate_page/generate.html',
                {
                    'form': QRCodeForm(),
                    'success': True,
                    'qr_image_url': qr_image_url
                }
            )
        else:
            print(qr_form.errors)

    return render(
        request= request,
        template_name= 'generate_page/generate.html',
        context= {'form': form}
    )