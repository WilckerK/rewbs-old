import os
from flask import Blueprint

# esse arquivo faz o from route import * importar todas as rotas e cria as blueprints

api = Blueprint("api", __name__)
dashboard = Blueprint("dashboard", __name__)
admin = Blueprint("admin", __name__)

def importRoutes():
  path = os.path.dirname(__file__)
  for route in os.scandir(path):
    if route.name.startswith("__"):
      continue 

    if route.is_file():
      string = f'import routes.{route.name}'[:-3]
      exec(string)
      continue
    
    for subRoute in os.scandir(f'{path}/{route.name}'):
      if subRoute.name.startswith("__"):
        continue 
      string = f'import routes.{route.name}.{subRoute.name}'[:-3]
      exec(string)