import random
# Listas de caracteres
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '@', '^']

print("--- Gerador de Senhas Seguras ---")

# Define o tamanho total MÍNIMO e MÁXIMO da senha
TAMANHO_MIN = 8
TAMANHO_MAX = 20

n_letras = int(input("quantas letras você quer na sua senha?"))
n_simbolos= int(input("quantos símbolos você quer na sua senha?"))
n_numeros= int(input("quatnso números você quer na sua senha?"))

senha= []
for _ in range(n_letras):
    caractere_aleatorio = random.choice(letras)
    senha.append(caractere_aleatorio)
for _ in range(n_simbolos):
    caractere_aleatorio = random.choice(numeros)
    senha.append(caractere_aleatorio)
for _ in range(n_numeros):
    caractere_aleatorio = random.choice(simbolos)
    senha.append(caractere_aleatorio)
random.shuffle(senha)
senha_final = "".join(senha)
print(f"sua senha é {senha_final}")

