from django.shortcuts import render

# Create your views here.
def render_plan_settings(request):
    return render(request = request, template_name = 'plan_settings/plan_settings.html')