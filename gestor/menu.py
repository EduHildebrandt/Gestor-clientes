""" Menú del programa """

import helpers
import manager

def loop():

    while True:

        helpers.clear()

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Agregar cliente     ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")

        helpers.clear()

        if option == '1':
            print("Listando los clientes...\n")
            manager.show_all()
        elif option == '2':
            print("Mostrando un cliente...\n")
            manager.find()
        elif option == '3':
            print("Agregando un cliente...\n")
            manager.add()
            print("Cliente agregado correctamente")
        elif option == '4':
            print("Modificando un cliente...\n")
            if manager.edit():
                print("Cliente modificado con exito...")
        elif option == '5':
            print("Borrando un cliente...\n")
            if manager.delete():
                print("Cliente borrado correctamente...")
        elif option == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")