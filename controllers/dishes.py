from flask import request
from flask_restful import Resource
from models.dish import Dish

class DishesAll(Resource):
    def get(self):
        dishes = Dish.query.filter_by(**request.args).all()
        return [dish.serialize() for dish in dishes]