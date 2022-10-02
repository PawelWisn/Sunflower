from django.shortcuts import render
from ordering.forms import OrderForm
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

def index(request):
    context = {"form": OrderForm()}
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Order receviced!"))
            return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, _("Order rejected! Please inspect form data. Remember to upload pictures only."))
            return redirect("index")
    
    return render(request, "index.html", context)