AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('\n>>>> Agenda vazia\n')


def buscar_contato(contato):
    try:
        print(f'{"-"*80}')
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereco:', AGENDA[contato]['endereco'])
        print(f'{"-"*80}')
    except KeyError:
        print('\n>>>> Contato inexistente\n')
    except Exception as error:
        print('\n>>>> Um erro inesperado ocorreu\n')
        print(error)


def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone':telefone,
        'email':email,
        'endereco':endereco, 
        }
    salvar()
    print(f'\n>>>> Contato {contato} adicionado/editado com sucesso.\n')


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f'\n>>>> Contato {contato} excluido com sucesso.\n')
    except KeyError:
        print('\n>>>> Contato inexistente\n')
    except Exception as error:
        print('\n>>>> Um erro inesperado ocorreu\n')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato};{telefone};{email};{endereco}\n')
        print('\n>>>> Agenda exportada com sucesso\n')
    except Exception as error:
        print('\n>>>> Algum erro ocorreu ao exportar contatos\n')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';') 

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('\n>>>> Arquivo não encontrado\n')
    except Exception as error:
        print('\n>>>> Algum erro inesperado aconteceu')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';') 

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone':telefone,
                    'email':email,
                    'endereco':endereco, 
                }
        print('\n>>>> Database carregado com sucesso\n')
        print(f'\n>>>> {len(AGENDA)} contatos carregados\n')
    except FileNotFoundError:
        print('\n>>>> Arquivo não encontrado\n')
    except Exception as error:
        print('\n>>>> Algum erro inesperado aconteceu')
        print(error)


def imprimir_menu():
    print(f'{"-"*80}\n'
         '1 - Mostrar todos os contatos da agenda\n'
         '2 - Buscar contato\n'
         '3 - Incluir contato\n'
         '4 - Editar contato\n'
         '5 - Excluir contato\n'
         '6 - Exportar contatos para CSV\n'
         '7 - Importar contatos de CSV\n'
         '0 - Fechar agenda\n'
        f'{"-"*80}')


# INICIO DO PROGRAMA
carregar()
while True:
    imprimir_menu()

    opcao = input('\nEscolha uma opção: ')

    print()

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('\n>>>>Contato já existente\n')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print(f'\n>>>> Editanto contato: {contato}\n')
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('\n>>>>Contato inexistente\n')
    
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    
    elif opcao == '0':
        print('\n>>>> Fechando o programa...')
        break
    else:
        print('\n>>>> Opção inválida\n')
