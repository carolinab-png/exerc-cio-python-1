# Seu código para obter o número e calcular o resto da divisão
numero = int(input("digite o número"))
resultado = numero % 2

# Aqui você vai usar o if-else
if resultado == 0:
    print("par")  # Apenas a linha 'print' precisa de indentação
else:
    print("impar") # E a linha 'print' do else também