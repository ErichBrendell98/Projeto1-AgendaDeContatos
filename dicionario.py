dicionario = {
    "tijolo":"objeto para construir muros",
    "constituição":"lei maxima do Brasil",
    "erich":24,
    "guilherme":19,
    "maria":17,
    "joão":20
    }
print(dicionario)
print(dicionario["tijolo"]) 
print(dicionario["constituição"])
print(dicionario["erich"])

for item in dicionario:
    print(f"\n{item}")

for item in dicionario.values():
    print(f"\n{item}")

for item in dicionario:
    print(f"\n{dicionario[item]}")