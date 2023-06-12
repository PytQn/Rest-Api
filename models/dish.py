from db import db


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    image = db.Column(db.String(5000))
    is_gluten_free = db.Column(db.Boolean, default=False)
    is_vegeterian = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "gluten":self.is_gluten_free,
            "vegeterian":self.is_vegeterian,
            "category":self.category.name
        }
