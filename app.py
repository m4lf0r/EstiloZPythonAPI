import os
from flask import Flask, request, send_from_directory
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

# Crie a aplicação Flask
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Garante que a pasta uploads exista

# Configure o CORS
CORS(app, resources={r"/*": {"origins": "*"}})

#Inicialize a API
api = Api(app, 
          version='1.0', 
          title='API da Loja EstiloZ', 
          description='Uma API para gerenciar os produtos da loja de roupas EstiloZ.',
          doc='/swagger',
          validate=True
)

ns_produtos = api.namespace('products', description='Operações relacionadas a produtos')

# parser para receber os dados do formulário
product_parser = ns_produtos.parser()
product_parser.add_argument('nome', type=str, required=True, help='Nome do produto', location='form')
product_parser.add_argument('preco', type=float, required=True, help='Preço do produto', location='form')
product_parser.add_argument('categoria_principal', type=str, required=True, help='Categoria principal', location='form')
product_parser.add_argument('sub_categoria', type=str, required=True, help='Sub-categoria', location='form')
product_parser.add_argument('imagem', type=FileStorage, location='files', help='Imagem do produto')

produto_model = ns_produtos.model('Produto', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'preco': fields.Float(required=True),
    'categoria_principal': fields.String(required=True),
    'sub_categoria': fields.String(required=True),
    'imagem_url': fields.String(description='URL da imagem do produto')
})

# Banco de dados em memória
PRODUTOS_DB = {
    1: {'nome': 'Casaco Moletom Branco e Rosa', 'preco': 129.90, 'categoria_principal': 'Feminino', 'sub_categoria': 'Casacos', 'imagem_url': ''},
    2: {'nome': 'Camiseta Anti Social Club Branca', 'preco': 79.90, 'categoria_principal': 'Unissex', 'sub_categoria': 'Camisetas', 'imagem_url': ''},
    3: {'nome': 'Boné Carros em Chamas', 'preco': 59.90, 'categoria_principal': 'Unissex', 'sub_categoria': 'Acessórios', 'imagem_url': ''},
    4: {'nome': 'Jaqueta Jeans Masculina', 'preco': 199.90, 'categoria_principal': 'Masculino', 'sub_categoria': 'Casacos', 'imagem_url': ''}
}
contador_id = 4

# ROTA PARA SERVIR AS IMAGENS
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@ns_produtos.route('/')
class ProductList(Resource):
    @ns_produtos.marshal_list_with(produto_model)
    def get(self):
        return [{'id': id, **data} for id, data in PRODUTOS_DB.items()]

    @ns_produtos.expect(product_parser)
    def post(self):
        """Cria um novo produto com imagem"""
        global contador_id
        args = product_parser.parse_args()

        imagem_url = ''
        imagem_file = args.get('imagem')

        if imagem_file and imagem_file.filename != '':
            filename = secure_filename(imagem_file.filename)
            imagem_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Construindo a URL que o frontend usará
            imagem_url = f"{request.host_url}uploads/{filename}"

        novo_produto_data = {
            'nome': args['nome'],
            'preco': args['preco'],
            'categoria_principal': args['categoria_principal'],
            'sub_categoria': args['sub_categoria'],
            'imagem_url': imagem_url
        }

        contador_id += 1
        PRODUTOS_DB[contador_id] = novo_produto_data
        
        # Retorne o dicionário diretamente
        return {'id': contador_id, **novo_produto_data}, 201

@ns_produtos.route('/<int:id>')
class Product(Resource):
    @ns_produtos.marshal_with(produto_model)
    def get(self, id):
        produto = PRODUTOS_DB.get(id)
        if produto:
            return {'id': id, **produto}
        api.abort(404, "Produto não encontrado")


    @ns_produtos.expect(product_parser)
    def post(self, id):
        """Atualiza um produto existente"""
        if id not in PRODUTOS_DB:
            api.abort(404, "Produto não encontrado")
        
        args = product_parser.parse_args()
        
        produto_existente = PRODUTOS_DB[id]
        imagem_url = produto_existente.get('imagem_url', '')

        imagem_file = args.get('imagem')
        if imagem_file and imagem_file.filename != '':
            filename = secure_filename(imagem_file.filename)
            imagem_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            imagem_url = f"{request.host_url}uploads/{filename}"

        dados_atualizados = {
            'nome': args['nome'],
            'preco': args['preco'],
            'categoria_principal': args['categoria_principal'],
            'sub_categoria': args['sub_categoria'],
            'imagem_url': imagem_url
        }

        PRODUTOS_DB[id] = dados_atualizados
        return {'id': id, **dados_atualizados}, 200

    def delete(self, id):
        """Deleta um produto"""
        if id in PRODUTOS_DB:
            del PRODUTOS_DB[id]
            return '', 204
        api.abort(404, "Produto não encontrado")


if __name__ == '__main__':
    app.run(debug=True)