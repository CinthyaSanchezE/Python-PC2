
"""
EJERCICIO MODULO 2
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
FECHA: 20/09/2025
"""

# PROBLEMA10: Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.
def factorial(n):
    if n < 0:
        return "El número debe ser un entero no negativo."
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número entero no negativo para el calculo: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

