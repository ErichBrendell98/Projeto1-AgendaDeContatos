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

def buscar_contato(contato):
    print(f'Nome: {contato}\n'
          f'Telefone: {AGENDA[contato]["telefone"]}\n'
          f'Email: {AGENDA[contato]["email"]}\n'
          f'Endereco: {AGENDA[contato]["endereco"]}\n'
          f'{"-"*80}')


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone':telefone,
        'email':email,
        'endereco':endereco, 
    }
    print(f'\n>>>> {contato} adicionado/editado com sucesso.\n')


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f'\n>>>> {contato} excluido com sucesso.\n')


def imprimir_menu():
    print(f'{"-"*80}\n'
         '1 - Mostrar todos os contatos da agenda\n'
         '2 - Buscar contato\n'
         '3 - Incluir contato\n'
         '4 - Editar contato\n'
         '5 - Excluir contato\n'
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
    elif opcao == '3' or opcao == '4':
        contato = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o email do contato: ')
        endereco = input('Digite o endereco do contato: ')
        incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '0':
        print('>>>> Fechando o programa...')
        break
    else:
        print('>>>> Opção inválida')
