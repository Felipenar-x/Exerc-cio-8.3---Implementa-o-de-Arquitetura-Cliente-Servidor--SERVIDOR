from flask import Flask, request, jsonify
from flask_cors import CORS 
from src.infrastructure.persist import TxtLivroRepository
from src.app.service import LivroService


app = Flask(__name__)
CORS(app)


repo = TxtLivroRepository("livros.txt", "banners.txt")
service = LivroService(repo)

@app.route('/api/livros', methods=['GET'])
def get_livros():
    """
    Endpoint que retorna o JSON com livros, banners e filtros.
    """
    categoria = request.args.get('categoria')
    busca = request.args.get('q')


    livros = service.listar_livros_com_notas(categoria, busca)
    banner = service.obter_banner()
    
    return jsonify({
        "livros": livros,
        "banner": banner,
        "categoria_atual": categoria,
        "busca": busca
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)