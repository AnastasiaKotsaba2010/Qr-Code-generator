from django.shortcuts import render

# Create your views here.
def render_generate(request):
    return render(request = request, template_name = 'generate_menu/generate_menu.html')