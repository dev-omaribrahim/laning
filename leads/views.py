from django.shortcuts import render
from .forms import LeadForm
from django.contrib import messages



def lead_creation(request):
    
    form = LeadForm()
    message = ""

    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم التسجيل")
        else:
            errors = form.errors
            messages.error(request, f"Errors: {errors}")
    
    context = {
        "form": form
    }

    return render(request, "leads/lead_form.html", context)

