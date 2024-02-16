
indice, soma, k = 13, 0, 0

while k < indice: # 0 a 12
    k = k + 1 
    soma = soma + k
    print(f"k is {k}")
    print(f"soma is {soma}")

# 91
print(soma) # k é 13 pq soma de 1 em 1, mas soma fica somando ela mesma + k, entao quando k for 1 a soma sera 1, quando k for 2 a soma = soma (1) + 2