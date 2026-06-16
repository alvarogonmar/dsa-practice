# Dado un arreglo de enteros nums y un entero target, devuelve los índices de los dos números que suman target.
# Ejemplo:

nums = [2, 7, 11, 15]
target = 9

# # Resultado esperado
# [0, 1]

# Porque:
# nums[0] + nums[1] == 9
# Restricciones para este primer intento
# ❌ No uses dict ni set.
# ✅ Intenta resolverlo con lo que sabes hasta ahora.

def twosum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    hash = {}
    for i in range(len(nums)):
        if nums[i] in hash:
            return [hash[nums[i]], i]
        else:
            hash[(target - nums[i])] = i
            
print(twosum(nums, target))