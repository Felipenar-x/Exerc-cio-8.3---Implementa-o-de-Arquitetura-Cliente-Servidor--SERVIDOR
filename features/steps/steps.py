from behave import given, when, then
from src.models import obter_livros, filtrar_livros

@given('que o banco de dados possui livros de "Suspense" e "Romance"')
def step_impl(context):
    context.lista_total = obter_livros()

@when('o usuário solicita a categoria "{categoria}"')
def step_impl(context, categoria):
    # Removi os colchetes daqui para enviar a STRING direto, 
    # como o seu models.py e app.py esperam.
    context.resultado = filtrar_livros(context.lista_total, categoria)

@then('o sistema retorna {quantidade:d} livro')
@then('o sistema retorna {quantidade:d} livros')
def step_impl(context, quantidade):
    assert len(context.resultado) == quantidade, f"Esperava {quantidade}, mas retornou {len(context.resultado)}"

@then('o título do livro é "{titulo}"')
def step_impl(context, titulo):
    titulos = [l['titulo'] for l in context.resultado]
    assert titulo in titulos, f"O livro {titulo} não foi encontrado"