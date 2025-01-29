from django.shortcuts import render

# Create your views here.
def render_generate(request):
    return render(request = request, template_name = 'generate/generate.html')