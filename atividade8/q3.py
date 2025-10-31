class Carro:
    def __init__(self, marca, modelo, ano, ligado):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if self.ligado == False:
            self.ligado= True
            print("o carro está ligado")
        else:	
            print("O carro já está ligado!")
        
    def desligar(self):
        if self.velocidade== 0:
                self.ligado = False
                print("o carro está desligado")
    def acelerar(self, valor):
        if self.ligado ==True:
            self.velocidade += valor
            print("o carro está acelerando")
    def frear(self, valor):
         if self.velocidade >0:
            nova_velocidade = self.velocidade - valor
            if nova_velocidade < 0:
                self.velocidade = 0
            else:
                self.velocidade = nova_velocidade
            print("o carro está freando")
    def exibir_informacoes(self):
        status = "Ligado" if self.ligado else "Desligado"
        print("--- INFORMAÇÕES DO CARRO ---")
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        print(f"Status: {status} | Velocidade: {self.velocidade} km/h")
        print("----------------------------")

# 1. Cria uma instância do carro (um objeto real)
meu_carro = Carro("Ford", "Ka", 2020, True) # Argumento 'ligado' é opcional, mas manter a consistência ajuda

print("--- TESTE DE FUNCIONALIDADE ---")

meu_carro.exibir_informacoes()

meu_carro.ligar()

meu_carro.desligar()

meu_carro.acelerar(40)

meu_carro.exibir_informacoes()

meu_carro.frear(40)

meu_carro.desligar()

print("--- FIM DO TESTE ---")