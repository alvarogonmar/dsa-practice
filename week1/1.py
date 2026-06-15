# Primer ejercicio (tipo entrevista)
# Sin usar sum() ni funciones similares, escribe una función que reciba una lista de enteros 
# y devuelva la suma de todos sus elementos.
# Ejemplo:
nums = [4, 7, 2, 9]
# Resultado esperado
# 22

def sumar(nums):
    resultado = 0
    for number in nums:
        resultado += number
    print(resultado)

sumar(nums)

# ¿Qué mejoraría en una entrevista?

# En lugar de imprimir el resultado, normalmente se espera que la función lo devuelva con return.

# def sumar(nums):
#     resultado = 0

#     for number in nums:
#         resultado += number

#     return resultado


# nums = [4, 7, 2, 9]
# print(sumar(nums))