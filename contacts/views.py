from django.shortcuts import render

# Create your views here.
def render_contacts(request):
    return render(request = request, template_name = 'contacts/contacts.html')