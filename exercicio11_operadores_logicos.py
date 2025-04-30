A = 1
B = 2
C = 3
X = 20
Y = 10
Z = -1

V1 = True
V2 = False

Nome = 'Pedro'
Rua = 'Pedrinho'

# Encontre o resultado das expressões lógicas abaixo:
# 1) A + C / B
print('1)' , A + C / B)

# 2) C / B / A
print('2)' , C / B / A)

# 3) -X ** B
print('3)' , -X ** B)

# 4) (-X) ** B
print('4)' , (-X) ** B)

# 5) V1 or V2
print('5)' , V1 or V2)

# 6) V1 and not V2
print('6)' , V1 and not V2)

# 7) V2 and not V1
print('7)' , V2 and not V1) # Ambos os lados precisam ser True para exibir um True

# 8) not Nome == Rua
print('8)' , not Nome == Rua)

# 9) V1 and not V2 or V2 and not True
print('9)', V1 and not V2 or V2 and not True)

# 10) X > Y and C <= B
print('10)' , X > Y and C <= B)

# 11) C - 3 * A < X = 2 * Z
print('11)' , C - 3 * A < X + 2 * Z)
