##Arquivo 1
try:
    arquivo = open('emails.txt')
    conteudo = arquivo.read()
    print(f'{type(arquivo)}\n{arquivo}\n{conteudo}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except:
    print('Algum erro ocorreu')
finally:
    arquivo.close()


##Arquivo 2
try:
    arquivo2 = open('emails.txt')
    conteudo2 = arquivo2.readlines()
    print(conteudo2)

    for linha in conteudo2:
        print(linha)

    print()

    for linha2 in conteudo2:
        print(linha2.strip())
except FileNotFoundError:
    print('Arquivo não encontrado')
except:
    print('Algum erro ocorreu')
finally:
    arquivo2.close()

print()


##Melhor forma de abrir arquivos
try:
    with open('emails.doc') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print('Arquivo não existe')


##Abrindo com permissão de escrita
try:
    with open('emails.txt', 'w') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print('Arquivo não existe')