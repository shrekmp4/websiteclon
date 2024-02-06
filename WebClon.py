import requests
from bs4 import BeautifulSoup
# By Shrekmp4 Support me at: https://github.com/shrekmp4
def clonar_sitio_web():
    url = input("Por favor, introduce la URL del sitio web que deseas clonar: ")

    # Obtener el contenido HTML del sitio web
    response = requests.get(url)
    html = response.text

    # Crear un objeto Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Guardar el contenido HTML clonado en un archivo
    with open('clon.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print('Sitio web clonado exitosamente!')

clonar_sitio_web()
