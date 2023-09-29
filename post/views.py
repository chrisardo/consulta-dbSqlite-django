from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry


# Create your views here.
def queries(request):
    # Obtiene todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrados por condicion
    filtered = Author.objects.filter(email="andrea26@example.net")

    # Obtener un unico elemento
    author = Author.objects.get(id=2)

    # Obteniendo los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener los 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    return render(
        request,
        "post/queries.html",
        {
            "authors": authors,
            "filtered": filtered,
            "author": author,
            "limits": limits,
            "offsets": offsets,
        },
    )
