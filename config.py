from dotenv import load_dotenv
import os

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    MONGODB_URI = os.getenv('MONGODB_URI') or 'mongodb://localhost:27017/db'
