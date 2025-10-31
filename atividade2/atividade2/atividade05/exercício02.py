nome = input("Digite seu nome: ")
while len(nome) < 4:
    print("Erro: O nome deve ter ao menos 4 caracteres.")
    nome = input("Digite seu nome novamente: ")
print("Nome OK!")
#idade
idade = int(input("Digite sua idade: "))
while idade < 1 or idade > 100:
    idade = int(input("Erro: A idade deve ser entre 1 e 100 anos.Digite sua idade novamente: "))
print("Idade OK!")
# salário
salário = float(input("digite seu salário"))
while salário <=0:
    salário = float(input("perdão, digite novamente seu salário"))
print("ok")
#gênero
genero_opcoes = ["F", "M", "O"]
genero = input("Digite seu gênero (F, M ou O): ")
while genero not in genero_opcoes:
    genero = input("Erro: Gênero inválido. Use F, M ou O.Digite seu gênero novamente: ")
print("ok")
#emprego
emprego = ["E", "D", "A"]
situacao_empregaticia = input("você está empregado(E), desempregado(D) ou é autônomo(A)")
while situacao_empregaticia not in emprego:
    situacao_empregaticia = input("Erro: situação inválida. Use E, D ou A:")
print("ok")