cardapio = {1: "coxinha - R$3", 2: "cachorro quente - R$ 5", 3: "suco - R$3"}

print("Bem-vindo ao nosso cardápio!")

# Exibe o cardápio de forma clara
for chave in cardapio:
    print(f"{chave} - {cardapio[chave]}")

# Solicita a escolha do usuário
pedido = int(input("Qual a sua escolha? Digite o número do item desejado: "))

# Valida a entrada
if pedido in cardapio:
    # Se a escolha for válida, exibe o item e o preço
    print(f"Você escolheu: {cardapio[pedido]}")
else:
    # Se a escolha for inválida, exibe a mensagem de erro
    print("Opção inválida. Por favor, escolha um item do cardápio.")