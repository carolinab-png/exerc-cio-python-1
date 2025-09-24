cidadeA = int(input("digite a população da primeira cidade:"))
cidadeB = int(input("digite a população da segunda cidade:"))
taxaA = int(input("digite a taxa de crescimento da primeira cidade:"))
taxaB = int(input("digite a taxa de crescimento da segunda cidade:"))

anos = 0

while cidadeA < cidadeB:
    cidadeA = cidadeA * (1 + taxaA)
    cidadeB = cidadeB * (1 + taxaB)
    anos = anos + 1
print(f"Serão necessários {anos} anos para a cidade A igualar ou ultrapassar a cidade B.")