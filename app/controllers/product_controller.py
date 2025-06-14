from flask_restx import Resource, fields, Namespace
from werkzeug.datastructures import FileStorage
from app import api
from app.services.product_service import produto_service # Importa o SERVICE

# Define o namespace
ns_produtos = Namespace('products', description='Operações relacionadas a produtos')

# Define o modelo para a documentação e respostas
produto_model = ns_produtos.model('Produto', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'preco': fields.Float(required=True),
    'categoria_principal': fields.String(required=True),
    'sub_categoria': fields.String(required=True),
    'imagem_url': fields.String()
})

# Define o parser para receber dados do formulário
product_parser = ns_produtos.parser()
product_parser.add_argument('nome', type=str, required=True, location='form')
product_parser.add_argument('preco', type=float, required=True, location='form')
product_parser.add_argument('categoria_principal', type=str, required=True, location='form')
product_parser.add_argument('sub_categoria', type=str, required=True, location='form')
product_parser.add_argument('imagem', type=FileStorage, location='files')

@ns_produtos.route('/')
class ProductList(Resource):
    @ns_produtos.marshal_list_with(produto_model)
    def get(self):
        return produto_service.get_all_products()

    @ns_produtos.expect(product_parser)
    @ns_produtos.marshal_with(produto_model, code=201)
    def post(self):
        """Cria um novo produto"""
        args = product_parser.parse_args()
        # Chama o método de CRIAÇÃO do service
        return produto_service.create_new_product(args)

@ns_produtos.route('/<int:id>')
class Product(Resource):
    @ns_produtos.marshal_with(produto_model)
    def get(self, id):
        return produto_service.get_product_by_id(id) or api.abort(404, "Produto não encontrado")

    @ns_produtos.expect(product_parser)
    @ns_produtos.marshal_with(produto_model)
    def post(self, id):
        """Atualiza um produto existente"""
        args = product_parser.parse_args()
        # Chama o método de ATUALIZAÇÃO do service
        produto = produto_service.update_existing_product(id, args)
        if produto:
            return produto
        api.abort(404, "Produto não encontrado")


    def delete(self, id):
        if produto_service.delete_product(id):
            return '', 204
        api.abort(404, "Produto não encontrado")