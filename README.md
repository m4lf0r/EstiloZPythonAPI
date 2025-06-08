<div align="center">
  <img src="https://i.imgur.com/Zdb3lgb.jpeg" width="150" alt="Logo EstiloZ](https://imgur.com/Zdb3lgb)">
  <h1>Projeto EstiloZ - API & Dashboard</h1>
  <p>Uma aplicação Full-Stack para gerenciamento de e-commerce de moda, com uma API RESTful em Python/Flask e um Dashboard interativo em JavaScript.</p>
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  </p>
</div>

---

## 📑 Sobre o Projeto

Este projeto foi desenvolvido como parte da avaliação da disciplina de **Desenvolvimento Backend** do curso de **Análise e Desenvolvimento de Sistemas** no **Centro Universitário Tiradentes (Unit - PE)**.

O objetivo foi criar uma solução completa que simula a gestão de produtos de uma loja online, aplicando conceitos modernos de arquitetura de software, como a separação de responsabilidades (Model-Service-Controller), a criação de APIs RESTful e a integração com um frontend dinâmico.

<br>

## ✨ Funcionalidades

<details>
  <summary><strong>🤖 Backend (API RESTful)</strong></summary>
  <ul>
    <li>✅ <strong>CRUD Completo de Produtos:</strong> Endpoints para Criar, Ler, Atualizar e Deletar produtos.</li>
    <li>🖼️ <strong>Upload de Imagens:</strong> Lógica para receber, salvar e servir imagens dos produtos.</li>
    <li>📚 <strong>Documentação Automática com Swagger:</strong> Interface interativa para testar e entender a API, gerada automaticamente pelo Flask-RESTX.</li>
    <li>🔐 <strong>CORS Habilitado:</strong> Configuração para permitir a comunicação segura com o frontend.</li>
    <li>🗂️ <strong>Arquitetura em Camadas:</strong> Código organizado em <strong>Model, Service e Controller</strong> para maior manutenibilidade e escalabilidade.</li>
  </ul>
</details>

<details>
  <summary><strong>🖥️ Frontend (Dashboard)</strong></summary>
  <ul>
    <li>📊 <strong>Interface Intuitiva:</strong> Um painel de controle claro e funcional para gerenciar todo o catálogo.</li>
    <li>📝 <strong>Formulário Dinâmico:</strong> Um único formulário para criar e editar produtos, com preenchimento automático para edições.</li>
    <li>🖼️ <strong>Visualização de Imagens:</strong> Exibição de miniaturas das imagens na tabela de produtos.</li>
    <li>🔗 <strong>Categorização Aninhada:</strong> Seleção de categoria principal que atualiza dinamicamente as opções de sub-categoria.</li>
    <li>🖌️ <strong>Ações Rápidas com Ícones:</strong> Botões de editar (lápis) e remover (lixeira) usando Font Awesome.</li>
  </ul>
</details>

<br>

## 🏛️ Arquitetura do Backend

Para atender aos requisitos de organização e boas práticas, o backend foi estruturado no padrão **Model-Service-Controller**:

-   **`Model (DAO)`**: Camada de acesso a dados. É a única que interage diretamente com a fonte de dados (no caso, um dicionário em memória).
-   **`Service`**: Camada que contém a lógica de negócio. Orquestra as operações, como salvar uma imagem no disco antes de pedir ao Model para salvar os dados do produto.
-   **`Controller`**: Camada de apresentação (HTTP). Recebe as requisições, valida os dados de entrada, chama o Service apropriado e formata a resposta HTTP.

```
/app
|-- /controllers
|   `-- product_controller.py
|-- /services
|   `-- product_service.py
|-- /models
|   `-- product_model.py
`-- __init__.py
```

<br>

## 🛠️ Instalação e Execução

Siga os passos abaixo para rodar a aplicação em seu ambiente local.

### Pré-requisitos
-   [Python 3.x](https://www.python.org/downloads/) e `pip`
-   [Git](https://git-scm.com/)
-   [Visual Studio Code](https://code.visualstudio.com/) com a extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/m4lf0r/EstiloZPythonAPI.git
    cd EstiloZPythonAPI
    ```

2.  **Instale as dependências do Backend:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Se o arquivo `requirements.txt` não existir, use: `pip install flask flask-restx flask-cors`)*

3.  **Inicie o Servidor Backend:**
    ```bash
    python run.py
    ```
    🎉 **API rodando!** Disponível em `http://127.0.0.1:5000`.

4.  **Inicie o Servidor Frontend:**
    -   Abra a pasta do projeto no VS Code.
    -   Clique com o botão direito no arquivo `frontend/dashboard.html`.
    -   Selecione **"Open with Live Server"**.

🎉 **Dashboard no ar!** Seu navegador abrirá em um endereço como `http://127.0.0.1:5500/frontend/dashboard.html`.

### URLs Importantes
-   **Dashboard:** `http://127.0.0.1:5500/frontend/dashboard.html`
-   **Documentação da API (Swagger):** `http://127.0.0.1:5000/swagger`

---

<div align="center">
  <p>Desenvolvido com ❤️ por <strong>EstiloZ</strong> para o <strong>Centro Universitário Tiradentes (Unit - PE)</strong></p>
</div>
