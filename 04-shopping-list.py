
shopping_list = [ ]
menu_option = ""

while menu_option !="4":

    print("lista de compras")
    print("1. agregar")
    print("2. quitar")
    print("3. ver")
    print("4. salir")
    menu_option = input()

    if menu_option == "1":

        #agregamos elementos a la lista
        shopping_list.append(input())

    elif menu_option == "2":

        element = input("ingresa el elemento a eliminar:  ")
        shopping_list.remove(element)   

    elif menu_option=="3":

        #motrar todo el contenido de shopping_list
        print("tu listado de compras tiene lo siguiente")
        for item in shopping_list:
            print(item)
    elif menu_option=="4":

        print("chao chao")

    else:
        
        print("selecciona una opcion valida")    
