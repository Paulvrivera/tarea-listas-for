#el while es la estructura e control, ue ejecuta una serie eentencia hata ue su conicion no se cumpla

fruits = ["chocolate","frugele","papas fritas"]

position = 0

while position < len(fruits):
    print(fruits[position])
    position += 1

print("-------------------")

for fruit in fruits:
    print(fruit)