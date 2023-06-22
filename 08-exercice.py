#cada estudiante del arreglo students tiene sus calificaciones en el arreglo grades ,manteniendo su posicion
students = ["ignacia","poulette","vane","jazz","tuguitugui"]  
Grades = [[5,6,4,5,6] ,[5,6,7,4,5],[5,6,4,5,6],[4,5,6,5,4],[5,6,4,5,6]]

#se pide un programa que imprima el nombre de la estudiante, junto con el promedio de su nota


# primero hay que calcular el promedio
position = 0
while position < len(students):
    student = students[position]#str
    student_grades = Grades [position]#list
    sum = 0
    position_two = 0
    while position_two < len(student_grades):
        sum += student_grades[position_two]
        position_two += 1
    print(f"El promedio de la estudiante {student} es: \n {sum/len(student_grades)}")
    position += 1

print("-------------------------")

for student in students:
    print(f"promedio de la estudiante es: {student[position]}")
