try:
    """
    WRITE MODE (w):
        Se o arquivo não existe, ele cria um novo
        Sobrescreve o arquivo existente
    """
    with open('nomes.txt', 'w') as arquivo:
        arquivo.write('Erich Brendell')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)

try:
    """
    APPEND MODE (a):
        Se o arquivo não existe, ele cria um novo
        Adiciona ao final do arquivo
    """
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('\nTeste\n')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)

"""
'r' - abre para ler
'w' - abre para escrever / arquivo é sobrescrito
'a' - abre para escrever / novo conteúdo é adicionado ao final do arquivo
'+' - pode ser escrito em conjunto com o 'r' por exemplo: 'r+' -> permite ler e escrever, mas se o arquivo não existe vai dar erro
'b' - para binário
"""