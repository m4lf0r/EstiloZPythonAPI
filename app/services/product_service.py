import os
from werkzeug.utils import secure_filename
from app import app # Para acessar a pasta de uploads
from app.models.product_model import produto_dao

class ProdutoService:
    def get_all_products(self):
        produtos = produto_dao.get_all()
        print(f"SERVICE.get_all_products retornando: {produtos}") # LOG
        return produtos

    def get_product_by_id(self, id):
        return produto_dao.get(id)

    def create_product(self, data):
        imagem_file = data.get('imagem')
        imagem_url = ''

        if imagem_file and imagem_file.filename != '':
            filename = secure_filename(imagem_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagem_file.save(filepath)
            imagem_url = filename # Salva apenas o nome do arquivo

        novo_produto_data = {
            'nome': data['nome'],
            'preco': data['preco'],
            'categoria_principal': data['categoria_principal'],
            'sub_categoria': data['sub_categoria'],
            'imagem_url': imagem_url
        }
        return produto_dao.create(novo_produto_data)

    def update_product(self, id, data):
        produto_existente = produto_dao.get(id)
        if not produto_existente:
            return None

        imagem_url = produto_existente.get('imagem_url', '')
        imagem_file = data.get('imagem')

        if imagem_file and imagem_file.filename != '':
            filename = secure_filename(imagem_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagem_file.save(filepath)
            imagem_url = filename
        
        dados_atualizados = {
            'nome': data['nome'],
            'preco': data['preco'],
            'categoria_principal': data['categoria_principal'],
            'sub_categoria': data['sub_categoria'],
            'imagem_url': imagem_url
        }
        
        print(f"SERVICE.update_product enviando para o DAO: ID={id}, DADOS={dados_atualizados}") # LOG
        
        return produto_dao.update(id, dados_atualizados)

    def delete_product(self, id):
        return produto_dao.delete(id)

produto_service = ProdutoService()