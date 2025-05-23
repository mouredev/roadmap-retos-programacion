# Proyecto de Simulación de Cola de Impresión

Este proyecto simula el funcionamiento de una **cola de impresión** utilizando la estructura de datos _cola (queue)_ en Python.

## 📋 Descripción

Permite al usuario:

- Agregar archivos a la cola de impresión.
- Imprimir documentos uno por uno en el orden en que fueron agregados (FIFO).
- Salir del programa cuando lo desee.

## 🖥️ Cómo usar el programa

Al ejecutar el script, se puede interactuar con las siguientes opciones:

- **agregar**: Agrega un archivo (por ejemplo, archivo.pdf) a la cola.
- **imprimir**: Procesa el archivo que esté primero en la cola.
- **salir**: Finaliza la ejecución del programa.

## 💡 Ejemplo de interacción

```text
Agrega un archivo o escribe: imprimir / salir: archivo.pdf
archivo.pdf ha sido agregado a la cola de impresión.

Agrega un archivo o escribe: imprimir / salir: archivo1.pdf
archivo1.pdf ha sido agregado a la cola de impresión.

Cola de impresión actual: ['archivo.pdf', 'archivo1.pdf']

Agrega un archivo o escribe: imprimir / salir: imprimir
Imprimiendo: archivo.pdf

Cola de impresión actual: ['archivo1.pdf']

Agrega un archivo o escribe: imprimir / salir: salir
Saliendo del programa.

```

![Demo de la cola de impresión](./demo_cola_impresion.gif)
