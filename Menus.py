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
    Manipulates.rm_contato(entrada)
    print(f'contato de numero:{entrada} foi removido da lista')

def menu_listar_contatos():
    print('====================')
    Manipulates.listar_contatos()

def menu_edit_contato():
    print('====================')
    numero_tel= input('digite o numero de telefone do contato a editar')
    print('campos:')
    print('1.numero de telefone')
    print('2.nome')
    print('3.idade')
    print('4.email')
    print('5.endereço')

    campo_editado= input('digite o numero do campo que vc quer editar')
    edit=input('coloque aqui a edição')
    if campo_editado == '1':
        Manipulates.edit_contato(numero_tel,campo_editado,edit)

    print(f'contato de numero de telefone:{numero_tel}, foi editado')