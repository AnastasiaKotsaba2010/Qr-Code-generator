import qrcode, os
from django.shortcuts import render, redirect
from django.http import HttpRequest
import qrcode.constants
from .forms import QRCodeForm
from .models import Qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import SolidFillColorMask

# Create your views here.

def generate_qr(request: HttpRequest):
    form = QRCodeForm()
    if request.method == 'POST':
        qr_form = QRCodeForm(request.POST, request.FILES)

        if qr_form.is_valid():
            print(000000)
            name = qr_form.cleaned_data.get('name')
            link = qr_form.cleaned_data.get('link')
            border = qr_form.cleaned_data.get('border')
            patterns = qr_form.cleaned_data.get('patterns')
            bg_color = qr_form.cleaned_data.get('bg_color')
            fg_color = qr_form.cleaned_data.get('fg_color')
            time = qr_form.cleaned_data.get('time')

            print(f'name: {name}, link: {link}, border: {border}')

            return render(
                request,
                'generate_page/generate.html',
                {
                    'form': qr_form,
                    # 'qr_image_path': file_path
                }
            )

    return render(
        request,
        'generate_page/generate.html',
        {'form': form}
    )