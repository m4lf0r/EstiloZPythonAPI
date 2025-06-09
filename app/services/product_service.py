import os
from werkzeug.utils import secure_filename
from app import app # Para acessar a pasta de uploads
from app.models.product_model import produto_dao

class ProdutoService:
    def get_all_products(self):
        return produto_dao.get_all()

    def get_product_by_id(self, id):
        return produto_dao.get(id)

    def _salvar_imagem(self, imagem_file):
        """Função auxiliar privada para salvar a imagem e retornar o nome do arquivo."""
        if imagem_file and imagem_file.filename != '':
            filename = secure_filename(imagem_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagem_file.save(filepath)
            return filename
        return None

    def create_new_product(self, data):
        """LÓGICA APENAS PARA CRIAÇÃO."""
        # Salva a imagem (se houver) e obtém o nome do arquivo
        nome_arquivo_imagem = self._salvar_imagem(data.get('imagem'))

        novo_produto_data = {
            'nome': data['nome'],
            'preco': data['preco'],
            'categoria_principal': data['categoria_principal'],
            'sub_categoria': data['sub_categoria'],
            'imagem_url': nome_arquivo_imagem or '' # Usa o novo nome ou uma string vazia
        }
        return produto_dao.create(novo_produto_data)

    def update_existing_product(self, id, data):
        """LÓGICA APENAS PARA ATUALIZAÇÃO."""
        produto_existente = produto_dao.get(id)
        if not produto_existente:
            return None

        # Salva a nova imagem (se houver)
        nome_arquivo_imagem = self._salvar_imagem(data.get('imagem'))

        # Prepara os dados para atualização
        dados_para_atualizar = {
            'nome': data['nome'],
            'preco': data['preco'],
            'categoria_principal': data['categoria_principal'],
            'sub_categoria': data['sub_categoria'],
        }

        # Só atualiza a imagem_url se uma nova imagem foi enviada
        if nome_arquivo_imagem:
            dados_para_atualizar['imagem_url'] = nome_arquivo_imagem
            
        return produto_dao.update(id, dados_para_atualizar)

    def delete_product(self, id):
        return produto_dao.delete(id)

produto_service = ProdutoService()