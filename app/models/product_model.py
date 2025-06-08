# Camada de Acesso a Dados (DAO)

PRODUTOS_DB = {
    1: {'nome': 'Casaco Moletom Branco e Rosa', 'preco': 129.90, 'categoria_principal': 'Feminino', 'sub_categoria': 'Casacos', 'imagem_url': 'CasacoMoletomBrancoERosa.png'},
    2: {'nome': 'Camiseta Anti Social Club Branca', 'preco': 79.90, 'categoria_principal': 'Unissex', 'sub_categoria': 'Camisetas', 'imagem_url': 'CamisetaBrancoERosa.png'},
    3: {'nome': 'Boné Carros em Chamas', 'preco': 59.90, 'categoria_principal': 'Unissex', 'sub_categoria': 'Acessórios', 'imagem_url': 'BoneCarrosEmChamas.png'},
    4: {'nome': 'Casaco Moletom Preto', 'preco': 199.90, 'categoria_principal': 'Masculino', 'sub_categoria': 'Casacos', 'imagem_url': 'CasacoMoletomPreto.png'}
}
contador_id = 4

class ProdutoDAO:
    def get_all(self):
        return [{'id': id, **data} for id, data in PRODUTOS_DB.items()]

    def get(self, id):
        produto_data = PRODUTOS_DB.get(id)
        if produto_data:
            return {'id': id, **produto_data}
        return None

    def create(self, produto_data):
        """
        Cria um novo produto. 'produto_data' deve ser um dicionário completo
        com todos os campos do produto (nome, preco, etc.).
        """
        global contador_id
        contador_id += 1
        
        # Garante que o ID não está no dicionário que será salvo
        novo_produto = produto_data.copy()
        
        PRODUTOS_DB[contador_id] = novo_produto
        
        # Retorna o produto recém-criado, já com o ID correto
        return {'id': contador_id, **novo_produto}

    def update(self, id, novos_dados):
        """
        Atualiza um produto existente. 'novos_dados' é um dicionário
        com os campos a serem atualizados.
        """
        if id in PRODUTOS_DB:
            # Pega o produto que já existe no "banco"
            produto_existente = PRODUTOS_DB[id]
            
            # Atualiza o dicionário existente com os novos dados
            produto_existente.update(novos_dados)
            
            # Retorna o produto completo e atualizado
            return {'id': id, **produto_existente}
        return None

    def delete(self, id):
        if id in PRODUTOS_DB:
            del PRODUTOS_DB[id]
            return True
        return False

produto_dao = ProdutoDAO()