import requests
from django.shortcuts import render
from .forms import ISBNForm
from .models import Libro


def agregar_libro(request):
    return render(request, 'libros/agregar_libro.html')


def agregar_libro(request):
    libro_info = None

    if request.method == 'POST':
        form = ISBNForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']

            # Realizar la solicitud a la API de Google Books
            url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
            response = requests.get(url)
            data = response.json()

            # Verificar si se obtuvieron resultados
            if 'items' in data:
                book_data = data['items'][0]['volumeInfo']
                libro_info = {
                    'titulo': book_data.get('title', 'No disponible'),
                    'autor': ', '.join(book_data.get('authors', ['No disponible'])),
                    'descripcion': book_data.get('description', 'No disponible'),
                    'isbn': isbn
                }
            else:
                libro_info = {'error': 'No se encontraron resultados para ese ISBN.'}

    else:
        form = ISBNForm()

    return render(request, 'libros/agregar_libro.html', {'form': form, 'libro_info': libro_info})
