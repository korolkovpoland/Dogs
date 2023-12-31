from django.shortcuts import render
from .models import Item

def dogs(request):
    items = Item.objects.all()
    book = {
        'items': items
    }
    return render(request, 'myapp/dogs.html', book)

def pet(request, id):
    items = Item.objects.get(id=id)
    book = {
        'pet': items
    }
    return render(request, 'myapp/pet.html', book)