import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave_padrão_para_dev')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:HwzOOWYKlFuIRNuYsXxshTZiARpRKbnZ@junction.proxy.rlwy.net:52831/railway"
    SQLALCHEMY_TRACK_MODIFICATIONS = False