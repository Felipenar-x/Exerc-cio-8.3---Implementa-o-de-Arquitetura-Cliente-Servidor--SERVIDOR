# language: pt
Funcionalidade: Busca de livros por categoria

Como um usuário
Quero filtrar livros por gênero
Para encontrar rapidamente o que me interessa

  Cenário: Filtrar livros por categoria de Suspense
    Dado que o banco de dados possui livros de "Suspense" e "Romance"
    Quando o usuário solicita a categoria "Suspense"
    Então o sistema retorna 6 livros
    E o título do livro é "O Silêncio dos Inocentes"

  Cenário: Categoria sem resultados
    Dado que o banco de dados possui livros de "Suspense" e "Romance"
    Quando o usuário solicita a categoria "Fantasia"
    Então o sistema retorna 7 livros