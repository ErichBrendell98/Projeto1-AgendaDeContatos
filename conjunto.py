conjunto_cores = {"vermelho", "azul", "verde"}
print(conjunto_cores)

for cor in conjunto_cores:
    print(cor)

# print(conjunto_cores[0])  => Conjunto não é ordenado

conjunto_cores.add("branco")
print(conjunto_cores)

conjunto_cores.add("vermelho")  #nesse caso, não funciona porque o conjunto não adiciona elementos repetidos
print(conjunto_cores)

conjunto_cores.remove("branco")
print(conjunto_cores)

conjunto_cores.clear()
print(conjunto_cores)