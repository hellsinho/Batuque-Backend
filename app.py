from flask import Flask
from models import db
from routes import auth
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)
CORS(app)

# Registrar Blueprint
app.register_blueprint(auth, url_prefix="/auth")

# Criar banco de dados na primeira execução
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
