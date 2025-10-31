class Pessoa:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos.")
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, matrícula):
        super().__init__(nome, idade)
        self.matrícula = matrícula
    def exibir_dados(self):
        print("\n--- Dados do Aluno ---")
        super().exibir_dados() 
        print(f"Matrícula: {self.matrícula}")
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def exibir_dados(self):
        print("\n--- Dados do Professor ---")
        super().exibir_dados() 
        print(f"Disciplina: {self.disciplina}")
aluno1 = Aluno("João Silva", 17, "A12345")
prof1 = Professor("Dra. Carla Souza", 45, "Matemática")

aluno1.exibir_dados()
prof1.exibir_dados()