idades = []
idade = int(input("Digite uma idade (ou -1 para parar): "))

while idade != -1:
    idades.append(idade)
    idade = int(input("Digite outra idade (ou -1 para parar): "))

contador_maiores = 0
for idade in idades:
    if idade >= 18:
        contador_maiores += 1

print(f"Você digitou {len(idades)} idades.")
print(f"O número de pessoas maiores de idade é: {contador_maiores}.")