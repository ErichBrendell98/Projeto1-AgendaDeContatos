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
    print(f'Nome: {contato}')
    print(f'Telefone: {AGENDA[contato]["telefone"]}')
    print(f'Email: {AGENDA[contato]["email"]}')
    print(f'Endereco: {AGENDA[contato]["endereco"]}')


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print(f'{"-"*80}')


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone':telefone,
        'email':email,
        'endereco':endereco, 
    }
    print(f'>>>>>> {contato} adicionado/editado com sucesso.')


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f'>>>>>> {contato} excluido com sucesso.')


incluir_editar_contato('joao', '987654321', 'joao@solyd.com.br', 'Av. 3')
incluir_editar_contato('erich', '555555555', 'contato@solyd.com.br', 'Av.1')
incluir_editar_contato('jose', '666666666', '', None)
excluir_contato('maria')
mostrar_contatos()

# buscar_contato('erich')