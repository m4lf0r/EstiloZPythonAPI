// URL base da sua API. Se o backend estiver rodando na mesma máquina, será esta.
//const API_BASE_URL = 'http://127.0.0.1:5000';
const API_BASE_URL = 'https://estiloz-api.onrender.com';

// Elementos do DOM que vamos manipular
const productTableBody = document.getElementById('product-table-body');
const productForm = document.getElementById('product-form');
const productIdInput = document.getElementById('product-id');
const nomeInput = document.getElementById('nome');
const precoInput = document.getElementById('preco');
const categoriaPrincipalInput = document.getElementById('categoria-principal');
const subCategoriaInput = document.getElementById('sub-categoria');
const formTitle = document.getElementById('form-title');

const subCategoriasMap = {
    'Masculino': ['Camisetas', 'Calças', 'Casacos'],
    'Feminino': ['Camisetas', 'Calças', 'Casacos', 'Vestidos'],
    'Unissex': ['Casacos', 'Camisetas','Acessórios', 'Bonés']
};


function atualizarSubCategorias() {
    const categoriaSelecionada = categoriaPrincipalInput.value;
    subCategoriaInput.innerHTML = '<option value="" disabled selected>-- Selecione --</option>'; // Limpa e adiciona o placeholder

    if (categoriaSelecionada && subCategoriasMap[categoriaSelecionada]) {
        const subCategorias = subCategoriasMap[categoriaSelecionada];
        subCategorias.forEach(sub => {
            const option = document.createElement('option');
            option.value = sub;
            option.textContent = sub;
            subCategoriaInput.appendChild(option);
        });
    }
}


categoriaPrincipalInput.addEventListener('change', atualizarSubCategorias);


// --- FUNÇÃO 1: BUSCAR E EXIBIR TODOS OS PRODUTOS ---
// Usa o método GET da API
async function fetchProducts() {
    try {
        const response = await fetch(`${API_BASE_URL}/products/`);
        if (!response.ok) throw new Error('Erro ao buscar produtos');
        const products = await response.json();

        // Limpa a tabela antes de preencher
        productTableBody.innerHTML = '';

        // Para cada produto, cria uma linha na tabela
        products.forEach(product => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>
                    ${product.imagem_url ? `<img src="${API_BASE_URL}/uploads/${product.imagem_url}" alt="${product.nome}" width="50">` : 'Sem Imagem'}
                </td>
                <td>${product.id}</td>
                <td>${product.nome}</td>
                <td>R$ ${product.preco.toFixed(2)}</td>
                <td>${product.categoria_principal}</td> 
                <td>${product.sub_categoria}</td>       
                <td class="actions-cell">

                    <button class="btn-action btn-edit" onclick='prepareEditForm(${JSON.stringify(product)})' title="Editar Produto">
                        <i class="fa-solid fa-pen-to-square"></i>
                    </button>

                    <button class="btn-action btn-delete" onclick='deleteProduct(${product.id})' title="Remover Produto">
                        <i class="fa-solid fa-trash"></i>
                    </button>

                </td>
            `;
            productTableBody.appendChild(tr);
        });
    } catch (error) {
        console.error('Falha na requisição:', error);
        alert(error.message);
    }
}

// --- FUNÇÃO 2: LIDAR COM O ENVIO DO FORMULÁRIO (CRIAR OU EDITAR) ---
productForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const id = productIdInput.value;
    const formData = new FormData();

    // Adiciona todos os campos do formulário ao FormData
    formData.append('nome', nomeInput.value);
    formData.append('preco', precoInput.value);
    formData.append('categoria_principal', categoriaPrincipalInput.value);
    formData.append('sub_categoria', subCategoriaInput.value);
    
    // Adiciona o arquivo de imagem, se um foi selecionado
    const imagemInput = document.getElementById('imagem');
    if (imagemInput.files[0]) {
        formData.append('imagem', imagemInput.files[0]);
    }
    
    const method = 'POST';
    const endpoint = id ? `${API_BASE_URL}/products/${id}` : `${API_BASE_URL}/products/`;

    try {
        const response = await fetch(endpoint, {
            method: method,
            body: formData, // Envia o FormData diretamente
        });

        if (!response.ok) {
            // Tenta ler o erro do backend se houver
            const errorData = await response.json();
            throw new Error(errorData.message || 'Erro ao salvar produto');
        }

        alert(`Produto ${id ? 'atualizado' : 'criado'} com sucesso!`);
        resetForm();
        fetchProducts();

    } catch (error) {
        console.error('Falha na requisição:', error);
        alert(error.message);
    }
});

// --- FUNÇÃO 3: DELETAR UM PRODUTO ---
// Usa o método DELETE da API
async function deleteProduct(id) {
    if (!confirm(`Tem certeza que deseja remover o produto com ID ${id}?`)) {
        return; // Se o usuário cancelar, não faz nada
    }

    try {
        const response = await fetch(`${API_BASE_URL}/products/${id}`, {
            method: 'DELETE',
        });
        if (!response.ok) throw new Error('Erro ao remover produto');

        alert('Produto removido com sucesso!');
        fetchProducts(); // Atualiza a tabela

    } catch (error) {
        console.error('Falha na requisição:', error);
        alert(error.message);
    }
}

// --- FUNÇÕES AUXILIARES ---

// Prepara o formulário para edição
function prepareEditForm(product) {
    formTitle.innerText = 'Editar Produto';
    productIdInput.value = product.id;
    nomeInput.value = product.nome;
    precoInput.value = product.preco;

    // Passo 1: Define a categoria principal
    categoriaPrincipalInput.value = product.categoria_principal;
    
    // Passo 2: Dispara a atualização das subcategorias
    atualizarSubCategorias();
    
    // Passo 3: Agora que o menu de subcategorias está preenchido, seleciona a correta
    subCategoriaInput.value = product.sub_categoria;
    
    window.scrollTo(0, 0); 
}

// Limpa o formulário
function resetForm() {
    formTitle.innerText = 'Adicionar Novo Produto';
    productForm.reset();
    productIdInput.value = ''; // Garante que o campo ID oculto seja limpo
}

// --- INICIALIZAÇÃO ---
// Chama a função para buscar os produtos assim que a página carrega
document.addEventListener('DOMContentLoaded', fetchProducts);