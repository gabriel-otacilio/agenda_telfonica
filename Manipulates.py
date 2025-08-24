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


def listar_contatos():
    for c in contatos:
        print(c)


def rm_contato(numero_tele):
    for i, d in enumerate(contatos):
        if d["numero de telefone"]:
            del contatos[i]
            break
