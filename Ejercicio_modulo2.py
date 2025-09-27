"""
EJERCICIO MODULO 2
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
FECHA: 20/09/2025
"""

# TEMA: COLECCION DE DATOS

# PROBLEMA1: Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente lista. Su programa debe retornar otra lista sin los duplicados.
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
def eliminar_duplicados(lista_original):
    lista_sin_duplicados = list(set(lista_original))
    return lista_sin_duplicados
resultado = eliminar_duplicados(lista_original)
print(resultado)

# PROBLEMA2: La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los 
# nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
# la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios, anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en la web. 
# Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin 
# importar el uso de mayúsculas y minúsculas) : - .gif - .jpg - .jpeg - .png - .pdf - .txt - .zip
# Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.
def obtener_tipo_mime(nombre_archivo):
    extensiones_mime = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    nombre_archivo = nombre_archivo.lower()
    for ext, mime in extensiones_mime.items():
        if nombre_archivo.endswith(ext):
            return mime
    return 'application/octet-stream'
nombre_archivo = input("Ingrese el nombre del archivo: ")
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME del archivo es: {tipo_mime}")

# PROBLEMA3: Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5, en el rango de 1500 y 2700 (ambos incluidos).
def divisibles():
    numeros = []
    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            numeros.append(num)
    return numeros
resultado = divisibles()
print(resultado)

# PROBLEMA4: Escriba un programa en Python para construir el siguiente patrón.
def imprimir_patron(n):
    for i in range(1, n + 1):
        print('* ' * i)
    for i in range(n - 1, 0, -1):
        print('* ' * i)
imprimir_patron(5)

# PROBLEMA5: Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números.
# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de números pares e impares.

def contar_pares_impares():
    numeros = []
    while True:
        respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
        if respuesta == 'SI':
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
        elif respuesta == 'NO':
            break
        else:
            print("Respuesta no válida. Por favor, responda con 'SI' o 'NO'.")
    
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = sum(1 for num in numeros if num % 2 != 0)
    
    print(f"Números ingresados: {numeros}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
contar_pares_impares()

# PROBLEMA6: Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
# materias. Puede usar el siguiente esquema a manera de ejemplo {Alumno: Juan, Notas: [10, 12, 15]} Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado completo de los alumnos.
def registrar_alumnos():
    alumnos = []
    while True:
        nombre = input("Ingrese el nombre del alumno (o 'fin' para terminar): ").strip()
        if nombre.lower() == 'fin':
            break
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la calificación {i + 1} para {nombre}: "))
            notas.append(nota)
        alumno = {'Alumno': nombre, 'Notas': notas}
        alumnos.append(alumno)
    
    print("\nListado completo de alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
registrar_alumnos()

# TEMA: FUNCIONES
# PROBLEMA7: Escribe un programa que encuentre la suma de todos los números primos menores que 100.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primos_menores():
    suma = 0
    for num in range(100):
        if es_primo(num):
            suma += num
    return suma
resultado = primos_menores()
print(f"La suma de todos los números primos menores que 100 es: {resultado}")

# PROBLEMA8: Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
def fibonacci():
    a, b = 0, 1
    serie = []
    while a <= 50:
        serie.append(a)
        a, b = b, a + b
    return serie
resultado = fibonacci()
print(f"La serie de Fibonacci entre 0 y 50 es: {resultado}")

# PROBLEMA9: Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo el propio número).
def es_perfecto(num):
    suma_divisores = sum(i for i in range(1, num) if num % i == 0)
    return suma_divisores == num
def numeros_perfectos():
    perfectos = []
    for num in range(1, 1000):
        if es_perfecto(num):
            perfectos.append(num)
    return perfectos
resultado = numeros_perfectos()
print(f"Números perfectos menores que 1000: {resultado}")



