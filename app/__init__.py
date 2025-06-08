import os
from flask import Flask, send_from_directory
from flask_restx import Api
from flask_cors import CORS

# 1. Crie e configure a aplicação Flask
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 2. Configure o CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# 3. Inicialize a API
api = Api(app,
          version='1.0',
          title='API da Loja EstiloZ',
          description='Uma API para gerenciar os produtos da loja de roupas EstiloZ.',
          doc='/swagger',
          validate=True
)

# 4. Importe e registre o namespace do controller
from app.controllers.product_controller import ns_produtos
api.add_namespace(ns_produtos)

# 5. Crie a rota para servir as imagens
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)