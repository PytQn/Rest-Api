from flask import Flask
from db import db
from flask_cors import CORS
from flask_restful import Api
from controllers.caterories import CategoryAll,CategoryOne
from controllers.dishes import DishesAll


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://restor:123Qwerty@myrestaurant.postgres.database.azure.com/postgres'
app.config['SECRET_KEY'] = 'dkfu5647lsemgs66jsdg34654'

CORS(app)
api = Api(app)

db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(DishesAll,'/dishes')
api.add_resource(CategoryAll,'/categories')
api.add_resource(CategoryOne,'/categories/<int:id>')

app.run(debug=True,host="0.0.0.0")