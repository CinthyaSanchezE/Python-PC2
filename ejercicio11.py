"""
EJERCICIO MODULO 2
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
FECHA: 20/09/2025
"""

# PROBLEMA 11: Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
# por ejemplo, omitiendo las vocales.Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
# texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.
# Ejemplo: - Input: Twitter Output: Twttr - Input: What's your name? Output: Wht's yr nm?
def omitir_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ''.join([letra for letra in texto if letra not in vocales])
    return resultado
texto_completo = input("Ingrese una cadena de texto: ")
texto_sin_vocales = omitir_vocales(texto_completo)
print(f"Texto sin vocales: {texto_sin_vocales}")