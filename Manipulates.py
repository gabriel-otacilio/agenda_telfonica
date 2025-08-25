from Contato import Contato
#import json

contatos = []


# def save():
#   with open("data/contatos.json", "w", encoding="utf-8") as f:
#      json.dump([c.to_dict() for c in contatos], f ,indent=4,ensure_ascii=False)

def adicionar_contato(nome, idade, email, numero_tel, endereco):
    contato1 = Contato(nome=nome, idade=idade, email=email, numero_de_tel=numero_tel, endereco=endereco)
    contatos.append(contato1.to_dict())
    # save()


def find_contato(numero):
    contato = next((d for d in contatos if d["numero de telefone"] == numero), None)
    # retorna o primeiro dicionário que satisfaz a condição
    return contato


def listar_contatos():
    for c in contatos:
        print(c)


def edit_contato(numero_tele, campo_editado, edit):# estou editando mas depois preciso apagar o antigo e escrever o novo
    contato_dict=find_contato(numero_tele)
    if campo_editado =='1':# editando o contato e salvando nele as diferenças
        contato_dict["numero de telefone"] = edit
    elif campo_editado =='2':#nome
        contato_dict["nome"] = edit
    elif campo_editado =='3':#idade
        contato_dict["idade"] = edit
    elif campo_editado =='4':#email
        contato_dict["email"] = edit
    elif campo_editado =='5':#endereço
        contato_dict["endereço"] = edit
    elif campo_editado =='0':#voltar/cancelar edição como fazer isso
        pass
    else:
        print('opção invalida')

    rm_contato(numero_tele)
    adicionar_contato(nome=contato_dict['nome'],idade=contato_dict['idade'],email=contato_dict['email'],numero_tel=contato_dict['numero de telefone'],endereco=contato_dict['endereço'])

def rm_contato(numero_tele):
    for i, c in enumerate(contatos):
        if c["numero de telefone"] == numero_tele:
            del contatos[i]
            break
