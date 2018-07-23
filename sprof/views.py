from django.shortcuts import render, render_to_response
from . forms import Contactform
# Create your views here.

def index(request):
    return render_to_response("sprof/index.html")

def contacts(request):
    contacts_form = Contactform()
    
    if request.method == 'POST':
        contacts_form = Contactform(data = request.form)
        if contacts_form.is_valid():
            Name = request.POST.get("name", '')
            Email = request.POST.get("email", '')
            Phone = request.POST.get("phone", '')
            message = request.POST.get("message", '')
            message.success(request,'Message sunmitted!')
            return redirect(contacts)
    else:
        contacts_form = Contactform()
    
    return render(request, "sprof/contact.html", {"form":contacts_form})