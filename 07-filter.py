grades = [4,5,6,7,8,3,4,5,6,7,2]

# como filtrar lo numeros pares y los impares
#pares
even = []
# impare
odd = []

#es para cuando el resto o residuo e dividir al numero en 2 es cero

for grade in grades:
    if grade % 2 == 0:
        even.append(grade)
    else:
        odd.append(grade)
    
print(f"Los pares son {even}")     
print(f"Los impares son {odd}")
 