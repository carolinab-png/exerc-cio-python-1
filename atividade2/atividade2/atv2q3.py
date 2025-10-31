import random

# Lista de opções
opcoes = ["pedra", "papel", "tesoura"]

# 1. Escolha do usuário
escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

# 2. Escolha do computador
escolha_computador = random.choice(opcoes)

print(f"Você escolheu: {escolha_usuario}")
print(f"O computador escolheu: {escolha_computador}")

# 3. Comparar e exibir o resultado
if escolha_usuario == escolha_computador:
    print("Empate!")
elif (
    (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
    (escolha_usuario == "papel" and escolha_computador == "pedra") or
    (escolha_usuario == "tesoura" and escolha_computador == "papel")
):
    print("Você venceu!")
else:
    print("O computador venceu.")