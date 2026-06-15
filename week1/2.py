# Ejercicio 2: Encontrar el número más grande
# Sin usar max(), escribe una función que reciba una lista de enteros y devuelva el número más grande.
# Ejemplo:
nums = [8, 3, 15, 1, 9]

# Resultado esperado
# 15

def maxi(nums):
    maximo = nums[0]
    for number in nums:
        if number > maximo:
            maximo = number
    return maximo

print(maxi(nums))
    