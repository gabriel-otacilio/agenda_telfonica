import Manipulates

def menu_add_contato():
    print("===================")
    nome=input("digite o nome do contato:")
    idade= input("digite a idade do contato")
    email= input("digite o e-mail do contato")
    endereco=input("digite o endereço do contato")
    numero_tel=input("digite o numero de telefone do contato")
    Manipulates.adicionar_contato(nome=nome,idade=idade,email=email,numero_tel=numero_tel,endereco=endereco)

def menu_rm_contato():
    print('====================')
    entrada= input("digite o numero de telefone do contato a excluir")

def menu_listar_contatos():
    print('====================')
    Manipulates.listar_contatos()