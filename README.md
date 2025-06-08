# 🛍️ Projeto Loja EstiloZ - API e Dashboard de Gerenciamento

Projeto universitário desenvolvido para a disciplina de **Desenvolvimento Backend** do curso de **Análise e Desenvolvimento de Sistemas** no **Centro Universitário Tiradentes (Unit)**.

A aplicação consiste em uma **API RESTful** construída com Python/Flask e um **Dashboard** (frontend) para gerenciar os produtos de uma loja de moda urbana fictícia, a "EstiloZ".

 <!-- Substitua pela URL de uma imagem do seu projeto -->

---

## ✨ Funcionalidades Principais

### Backend (API RESTful)
- ✅ **CRUD Completo de Produtos:** Crie, liste, busque, atualize e delete produtos.
- 🖼️ **Upload de Imagens:** Endpoint dedicado para upload de imagens associadas aos produtos.
- 📚 **Documentação Automática:** Geração de documentação interativa com **Swagger UI** através do Flask-RESTX.
- 🔐 **CORS Habilitado:** Permite a comunicação segura com o frontend que roda em outro domínio/porta.
- 🗂️ **Categorização Aninhada:** Suporte para categorias principais (Masculino, Feminino) e sub-categorias (Camisetas, Calças).

### Frontend (Dashboard)
- 📊 **Interface Intuitiva:** Um painel de controle para gerenciar todo o catálogo de produtos.
- 📝 **Formulário Dinâmico:** Formulário único para criar e editar produtos, com os dados carregados automaticamente para edição.
- 🖼️ **Visualização de Imagens:** Exibição de miniaturas das imagens dos produtos na tabela.
-  एक्शन **Ações Rápidas:** Botões com ícones (usando Font Awesome) para editar e remover produtos de forma ágil.
- 📱 **Design Responsivo:** Layout que se adapta a diferentes tamanhos de tela.

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Linguagem principal da API. |
| | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Micro-framework web para a construção da API. |
| | **Flask-RESTX** | Extensão para criar APIs RESTful e gerar documentação Swagger. |
| | **Flask-Cors** | Extensão para lidar com políticas de Cross-Origin Resource Sharing. |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | Estrutura da página do dashboard. |
| | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | Estilização da interface. |
| | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | Interatividade e comunicação com a API (Fetch API, async/await). |
| **Ambiente** | ![Visual Studio Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white) | Editor de código utilizado no projeto. |
| | **Live Server** | Extensão do VS Code para servir o frontend e habilitar live-reload. |

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

### Pré-requisitos
- [Python 3.x](https://www.python.org/downloads/)
- `pip` (gerenciador de pacotes do Python)
- [Visual Studio Code](https://code.visualstudio.com/) (recomendado) com a extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).

### 1. Backend

Primeiro, clone o repositório e configure o servidor da API.

```bash
# Clone este repositório
git clone https://github.com/m4lf0r/EstiloZPythonAPI

# Navegue até a pasta do projeto
cd seu-repositorio

# Instale as dependências do Python
pip install flask flask-restx flask-cors

# Inicie o servidor da API
python app.py
```
🎉 O backend estará rodando em `http://127.0.0.1:5000`.

### 2. Frontend

Em uma nova janela do terminal ou diretamente no VS Code:

1.  Abra a pasta do projeto no **Visual Studio Code**.
2.  No explorador de arquivos, clique com o botão direito no arquivo `frontend/dashboard.html`.
3.  Selecione a opção **"Open with Live Server"**.

🎉 O seu navegador abrirá automaticamente o dashboard, geralmente em `http://127.0.0.1:5500/frontend/dashboard.html`.

### 3. Acessando os Recursos

-   **Dashboard:** `http://127.0.0.1:5500/frontend/dashboard.html`
-   **Documentação da API (Swagger):** `http://127.0.0.1:5000/swagger`

---


-   **UNIT-PE**
