AGENDA = {
    "erich":{
        "tel":"99999-1010",
        "email":"contato@solyd.com.br",
        "endereco":"av. 1"
    },
    "maria":{
        "tel":"99229-2020",
        "email":"maria@solyd.com.br",
        "endereco":"av. 2"
    },
    "joao":{
        "tel":"98267-6060",
        "email":"joao@solyd.com.br",
        "endereco":"av. 3"
    },
}

print(AGENDA["maria"])
print(AGENDA["erich"]['tel'])
print(AGENDA["joao"]['endereco'])

AGENDA["erich"]["endereco"] = "Rua das Nações"
print(AGENDA["erich"])

AGENDA["lucas"] = {
    "tel":"98567-5621",
    "email":"lucas@solyd.com.br",
    "endereco":"ave. jose bonifacio",
}

for contato in AGENDA:
    print(contato)

print(AGENDA["lucas"])

AGENDA.pop("lucas")

for contato in AGENDA:
    print(contato)