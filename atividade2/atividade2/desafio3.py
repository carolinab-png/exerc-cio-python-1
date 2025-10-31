print("Bem vindo à pizzaria!")
tamanho = input("Qual o tamanho você quer? P, M ou G?")

if tamanho == "P":  
    preco_final = 15
elif tamanho == "M":
    preco_final = 20
else:
    preco_final = 25
adição_de_pepperoni = input("você quer acrescentar pepperoni? (S/N)")
if adição_de_pepperoni == "S":
    preco_final= preco_final + 3
queijo_extra = input("você quer queijo extra? (S/N)")
if queijo_extra == "S":
    preco_final = preco_final + 1
print(f"o preço final da sua pizza é R$ {preco_final}")

