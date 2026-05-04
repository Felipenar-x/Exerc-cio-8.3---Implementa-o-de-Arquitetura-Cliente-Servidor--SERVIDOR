from datetime import datetime

class LivroService:
    def __init__(self, repository): # Injeção de Dependência
        self.repository = repository

    def listar_livros(self, categoria=None, nome=None):
        dados = self.repository.obter_todos()
        
        if categoria:
            dados = [l for l in dados if l["categoria"].lower() == categoria.lower()]
        if nome:
            dados = [l for l in dados if nome.lower() in l["titulo"].lower()]
        return dados

    def obter_banner(self):
        mes_atual = datetime.now().month
        promocoes = self.repository.obter_promocoes()
        for promo in promocoes:
            if promo["mes"] == mes_atual:
                return promo
        return None
    def obter_detalhes_livro(self, titulo_livro):
        todas = self.repository.obter_avaliacoes()
        return [a for a in todas if a["titulo"] == titulo_livro]
    

    def listar_livros_com_notas(self, categoria=None, nome=None):
        livros = self.listar_livros(categoria, nome)
        avaliacoes = self.repository.obter_avaliacoes()
        
        for livro in livros:
            notas_do_livro = [a for a in avaliacoes if a["titulo"].strip() == livro["titulo"].strip()]
            livro["avaliacoes"] = notas_do_livro  # Agora é no plural!
            
        return livros