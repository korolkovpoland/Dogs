from django.shortcuts import render
from .models import Item

def dogs(request):
    items = Item.objects.all()
    book = {
        'items': items
    }
    return render(request, 'myapp/dogs.html', book)