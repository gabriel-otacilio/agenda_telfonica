from Contato import Contato
import json

contatos = []

# def save():
#   with open("data/contatos.json", "w", encoding="utf-8") as f:
#      json.dump([c.to_dict() for c in contatos], f ,indent=4,ensure_ascii=False)

def adicionar_contato(nome, idade, email, numero_tel, endereco):
    contato1 = Contato(nome=nome, idade=idade, email=email, numero_de_tel=numero_tel, endereco=endereco)
    contatos.append(contato1.to_dict())
    # save()
def find_contato(numero):
    contato = next((d for d in contatos if d["numero de telefone"] == numero),None)
    #retorna o primeiro dicionário que satisfaz a condição
    return contato

def listar_contatos():
    for c in contatos:
        print(c)

def edit_contato(numero_tele,campo_editado,edit):
    for c in contatos:
        if c["numero de telefone"] == numero_tele:
            if campo_editado == '1':
                pass #TODO tem como editar um campo de um dicionário sem transformar pra objeto denovo

def rm_contato(numero_tele):
    for i, c in enumerate(contatos):
        if c["numero de telefone"] == numero_tele:
            del contatos[i]
            break
