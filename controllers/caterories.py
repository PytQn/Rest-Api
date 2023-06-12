from flask_restful import Resource
from models.category import Category

class CategoryAll(Resource):
    def get(self):
        categories = Category.query.all()
        return [category.serialize() for category in categories]
    
class CategoryOne(Resource):
    def get(self,id):
        category = Category.query.get(id)
        return category.serialize()