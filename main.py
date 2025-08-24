
import Menus

def menu():
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
       Menus.menu_add_contato()#check
    elif entrada == "2":
        Menus.menu_rm_contato()#check
    #elif entrada == "3":
    elif entrada == "4":
        Menus.menu_listar_contatos()#check
    #elif entrada == "5":
    elif entrada == "0":
        break
    else:
        print("opção invalida")






