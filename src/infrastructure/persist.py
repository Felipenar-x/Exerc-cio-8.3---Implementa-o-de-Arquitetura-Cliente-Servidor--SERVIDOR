from src.domain.repositorio import ILivroRepository

class TxtLivroRepository(ILivroRepository):
    def __init__(self, arquivo_livros="livros.txt", arquivo_promos="promocoes.txt"):
        self.arquivo_livros = arquivo_livros
        self.arquivo_promos = arquivo_promos

    def obter_todos(self):
        livros = []
        try:
            with open(self.arquivo_livros, "r", encoding="utf-8") as f:
                for linha in f:
                    if linha.strip():
                        titulo, categoria = linha.strip().rsplit(",", 1)
                        livros.append({"titulo": titulo, "categoria": categoria})
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.arquivo_livros} não encontrado.")
        return livros

    def obter_promocoes(self):
        promos = []
        try:
            with open(self.arquivo_promos, "r", encoding="utf-8") as f:
                for linha in f:
                    if linha.strip():
                        # O formato no TXT é: Evento,Desconto,Mês,Cor
                        evento, desconto, mes, cor = linha.strip().split(",")
                        promos.append({
                            "evento": evento,
                            "desconto": desconto,
                            "mes": int(mes), # Convertemos para inteiro para comparar com o mês atual
                            "cor": cor
                        })
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.arquivo_promos} não encontrado.")
        return promos

    def obter_avaliacoes(self):
        notas = []
        try:
            with open("avaliacao.txt", "r", encoding="utf-8") as f: 
                for linha in f:
                    if linha.strip():

                        titulo, nota, texto = linha.strip().split(",", 2) 
                        notas.append({
                            "titulo": titulo.strip(), 
                            "nota": nota.strip(), 
                            "texto": texto.strip()
                        })
        except FileNotFoundError:
            return []
        return notas