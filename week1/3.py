# Ejercicio 3 (muy común en entrevistas)
# Dada una lista de enteros, devuelve True si contiene algún elemento duplicado y False en caso contrario.

# Ejemplos:
nums1 = [1, 2, 3, 4]      # -> False
nums2 = [1, 2, 3, 1]     # -> True
# [7]               -> False
# [5, 5]            -> True

# def dupli(nums):
#     duplis = []
#     for number in nums:
#         if number in duplis:
#             return True
#         else:
#             duplis.append(number)
#     return False

def dupli(nums):
    vistos = set()
     
    for number in nums:
        if number in vistos:
            return True
        else:
            vistos.add(number)
    return False

print(dupli(nums1))
print(dupli(nums2))
