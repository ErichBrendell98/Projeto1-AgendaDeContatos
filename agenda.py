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
    for contato in AGENDA:
        print(f"Nome: {contato}")
        print(f"Telefone: {AGENDA[contato]['telefone']}")
        print(f"Email: {AGENDA[contato]['email']}")
        print(f"Endereco: {AGENDA[contato]['endereco']}")
        print(f'{"-"*80}')

mostrar_contatos()