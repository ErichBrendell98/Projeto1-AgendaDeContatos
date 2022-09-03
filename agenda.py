AGENDA = {}

AGENDA['erich'] = {
    'telefone':'999991234',
    'email':'erich@solyd.com.br',
    'endereco':'Av. 1',
}

AGENDA['maria'] = {
    'telefone':'988885678',
    'email':'maria@solyd.com.br',
    'endereco':'Av. 2',
}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('\n>>>> Agenda vazia\n')

def buscar_contato(contato):
    try:
        print(f'Nome: {contato}\n'
            f'Telefone: {AGENDA[contato]["telefone"]}\n'
            f'Email: {AGENDA[contato]["email"]}\n'
            f'Endereco: {AGENDA[contato]["endereco"]}\n'
            f'{"-"*80}')
    except KeyError:
        print('\n>>>> Contato inexistente\n')
    except Exception as error:
        print('\n>>>> Um erro inesperado ocorreu\n')
        print(error)



def incluir_editar_contato(contato):
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')

    AGENDA[contato] = {
        'telefone':telefone,
        'email':email,
        'endereco':endereco, 
        }
    print(f'\n>>>> {contato} adicionado/editado com sucesso.\n')


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print(f'\n>>>> Contato {contato} excluido com sucesso.\n')
    except KeyError:
        print('\n>>>> Contato inexistente\n')
    except Exception as error:
        print('\n>>>> Um erro inesperado ocorreu\n')
        print(error)

def exportar_contatos():
    try:
        with open('agenda.csv', 'w') as arquivo:
            arquivo.write('nome;telefone;email;endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato};{telefone};{email};{endereco}\n')
        print('\n>>>> Agenda exportada com sucesso\n')
    except Exception as error:
        print('\n>>> Algum erro ocorreu ao exportar contatos\n')
        print(error)

def imprimir_menu():
    print(f'{"-"*80}\n'
         '1 - Mostrar todos os contatos da agenda\n'
         '2 - Buscar contato\n'
         '3 - Incluir contato\n'
         '4 - Editar contato\n'
         '5 - Excluir contato\n'
         '6 - Exportar contatos para CSV\n'
         '0 - Fechar agenda\n'
        f'{"-"*80}')


while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
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
            incluir_editar_contato(contato)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print(f'\n>>>>Editanto contato {contato}\n')
            incluir_editar_contato(contato)
        except KeyError:
            print('\n>>>>Contato inexistente\n')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exportar_contatos()
    elif opcao == '0':
        print('\n>>>> Fechando o programa...')
        break
    else:
        print('\n>>>> Opção inválida\n')
