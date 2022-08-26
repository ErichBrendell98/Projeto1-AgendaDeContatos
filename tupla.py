"""
Tuplas: São imutáveis e também mais rápidas que listas
"""

tuplaCores = ("amarelo", "azul", "roxo")
listaCores = ["amarelo", "azul", "roxo"]

listaCores.append("vermelho")

print(tuplaCores)
print(listaCores)
print(tuplaCores.count("azul"))

listaCores[1] = "branco"
print(listaCores)

for cor in tuplaCores:
    print(cor)
