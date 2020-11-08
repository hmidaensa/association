import form as form
from django.shortcuts import render,redirect
from .forms import SaisonForm
# Create your views here.

def saison_list(request):
    if request == "GET":
        form = SaisonForm()
        return render(request, "gerer_saison/create_saison.html", {'form': form})

    elif request == "POST":
        form = SaisonForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "gerer_saison/create_saison.html", {'form': form})





def saison_form(request):
    if request == "GET":
        form = SaisonForm()
        return render(request, "gerer_saison/create_saison.html", {'form': form})

    elif request == "POST":
        form = SaisonForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "gerer_saison/create_saison.html", {'form': form})
    else:
        form = SaisonForm()
        return render(request, "gerer_saison/create_saison.html", {'form': form})







