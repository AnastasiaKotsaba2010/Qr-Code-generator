from django.shortcuts import render

# Create your views here.
def render_auth(request):
    return render(request = request, template_name = 'authorization/auth.html') 