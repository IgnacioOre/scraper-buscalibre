# scraper-buscalibre
Simple scraping de libros en Buscalibre con Python y Beautiful Soup. A partir de una URL de Buscalibre.cl, extrae título, autor y precio de todos los libros para esa sección.

## Ejecución
```
py buscalibre.py [URL]
```

Donde URL es una dirección válida de Buscalibre de algún apartado de libros en venta.

## Ejemplo
Los resultados de oferta.csv fueron conseguidos ejecutando

```
py buscalibre.py https://www.buscalibre.cl/libros-envio-express-chile_t.html
```
Corresponden a los libros con envío en un día dentro de Chile.
