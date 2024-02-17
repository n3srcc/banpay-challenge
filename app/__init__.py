from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from config import Config
import yaml

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

from app.routes.users import users_bp
from app.routes.services import service_bp

app.register_blueprint(service_bp, url_prefix='/api')
app.register_blueprint(users_bp, url_prefix='/api')

with open("./app/routes/swagger_docs/api_docs.yaml", "r") as file:
    api_docs = yaml.load(file, Loader=yaml.FullLoader)

swagger = Swagger(app, template=api_docs)
