from django.shortcuts import render

# Create your views here.
def render_my_QrCode(request):
    return render(request = request, template_name = 'my_QrCode/my_QrCode.html')