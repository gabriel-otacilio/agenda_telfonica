import Menus
#TODO introduzir o voltar nos menus
#

def menu():
    print('Bem vindo a sua agenda telefonica, por favor escolha uma das funcionalidades do sistema')
    print("1.adicionar contato")
    print("2.remover contato")
    print("3.editar contato")
    print("4.listar contatos")
    print("5.buscar contato")
    print("0.sair")


while True:
    menu()
    entrada = input("escolha uma opção")
    if entrada == "1":
        Menus.menu_add_contato()  # check
    elif entrada == "2":
        Menus.menu_rm_contato()  # check
    elif entrada == "3":
        Menus.menu_edit_contato()  #check
    elif entrada == "4":
        Menus.menu_listar_contatos()  # check
    elif entrada == "5":
        Menus.menu_find_contato()  # check
    elif entrada == "0":
        break
    else:
        print("opção invalida")
