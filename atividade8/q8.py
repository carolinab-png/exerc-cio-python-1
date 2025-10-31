class ExportadorDeDados:
    def __init__(self, caminho_arquivo):
        # Seu código aqui para armazenar o atributo
        self.caminho_arquivo = caminho_arquivo
    
    def exportar(self, dados):
        raise NotImplementedError
    
class ExportadorParaCSV(ExportadorDeDados):
    def __init__(self, caminho_arquivo):
        super().__init__(caminho_arquivo)
    def exportar(self, dados):
        with open(self.caminho_arquivo, 'w') as arquivo:
            chaves = dados[0].keys()
            arquivo.write(",".join(chaves))
            for item in dados:
                valores = [str(v) for v in item.values()]
                arquivo.write(",".join(valores)+"\n")
        print(f"✅ Exportado para CSV: {self.caminho_arquivo}")

class ExportadorParaTXT(ExportadorDeDados):

    def exportar(self, dados):
        with open(self.caminho_arquivo, 'w') as arquivo:
            arquivo.write("--- Relatório de Usuários ---\n")
            
            for i, item in enumerate(dados):
                arquivo.write("-" * 20 + f"\nUsuário {i+1}:\n")
                
                for chave, valor in item.items():
                    arquivo.write(f"{chave}: {valor}\n")
                    
        print(f"✅ Exportado para TXT: {self.caminho_arquivo}")

def gerar_relatorios(exportadores, dados):
    """
    Chama o método 'exportar' de cada objeto na lista.
    Esta função é FLEXÍVEL (Polimorfismo).
    """
    print("\n--- Iniciando Geração de Relatórios ---")
    
    for exportador in exportadores:
        # A magia do Polimorfismo: o mesmo comando (exportador.exportar) 
        # executa o código certo para CSV ou para TXT.
        exportador.exportar(dados)
    
    print("--- Geração Concluída ---")