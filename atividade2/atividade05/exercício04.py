# Passo 1: Definindo as variáveis iniciais
# População das cidades e suas taxas de crescimento anuais em decimal
cidadeA = 90000
cidadeB = 250000
taxaA = 0.035
taxaB = 0.012

# Variável para contar o número de anos, começando em zero
anos = 0

# Passo 2: O laço de repetição
# O laço roda enquanto a população da cidade A for menor que a da cidade B
while cidadeA < cidadeB:
    # Passo 3: O que acontece a cada ano
    # Atualiza a população da cidade A
    cidadeA = cidadeA * (1 + taxaA)

    # Atualiza a população da cidade B
    cidadeB = cidadeB * (1 + taxaB)

    # Incrementa o contador de anos
    anos = anos + 1

# Passo 4: O resultado final
# Exibe a quantidade de anos necessários
print(f"Serão necessários {anos} anos para a cidade A igualar ou ultrapassar a cidade B.")