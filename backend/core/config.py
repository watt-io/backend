from dotenv import dotenv_values

config = dotenv_values('.env')

SECRET_KEY = config.get('SECRET_KEY', None)
PROJECT_NAME = config.get('PROJECT_NAME', None)
DEBUG = config.get('DEBUG', None)
