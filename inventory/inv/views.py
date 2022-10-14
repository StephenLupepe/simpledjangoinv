from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Items

def home(request):
    context = {'items': Items.objects.all()}
    return render(request, "inv/home.html", context)

class AddItemView(CreateView):
    model = Items
    fields = ["name", "desc", "type", "num"]
    success_url = "/"

class ItemDetailView(DetailView):
    model = Items

class ItemUpdateView(UpdateView):
    model = Items
    fields = ["name", "desc", "type", "num"]
    success_url = "/"
    template_name = "inv/items_update.html"

class ItemDeleteView(DeleteView):
    model = Items
    success_url = "/"
    template_name = "inv/items_confirm_delete.html"