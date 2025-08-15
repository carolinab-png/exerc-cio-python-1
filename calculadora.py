n1= input("digite o primeiro número")
n2= input("digite o segundo número")
número1= int(n1)
número2= int(n2)
soma = número1 + número2
subtração = número1 - número2
multiplicação = número1 * número2
if número2 != 0:
    divisao = número1 / número2
else:
    divisao = None
    print(f"A soma de {número1} e {número2} é: {soma}")
print(f"A subtração de {número1} por {número2} é: {subtração}")
print(f"A multiplicação de {número1} por {número2} é: {multiplicação}")

if divisao is not None:
    print(f"A divisão de {número1} por {número2} é: {divisao}")
else:
    print("Não é possível dividir por zero.")
