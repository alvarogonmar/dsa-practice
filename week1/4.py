nums = [4, 7, 2, 9, 6]
def minimo(nums):
    minimo = nums[0]

    for number in nums:
        if number < minimo:
            minimo = number
    return minimo

def promedio(nums):
    suma = 0
    for number in nums:
        suma += number
    suma = suma / len(nums)
    return suma

def contar_pares(nums):
    pares = 0
    for number in nums:
        if number % 2 == 0:
            pares += 1
    return pares



print(minimo(nums))       # 2
print(promedio(nums))     # 5.6
print(contar_pares(nums)) # 3