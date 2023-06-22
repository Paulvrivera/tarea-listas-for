grades = [ ]
menu_option = ""
while menu_option !="3":
    print("calculadora de promedio")
    print("1. agregar nota")
    print("2. calcular promedio")
    print("3. salir")

    menu_option = input()

    if menu_option == "1":
        number = float(input("ingresa la nota"))
        grades.append(number)
    elif menu_option == "2": 
        #sumar todas  las notas y dividir por la cantidad
        position = 0

        #acumulador
        sum = 0
        for grade in grades :
            sum += grade
        print(f"El promedio es la nota es {sum/len(grades)}")    
    elif menu_option =="3":
        print("chaucito")
    else:
        print("ingrese algo valido")        