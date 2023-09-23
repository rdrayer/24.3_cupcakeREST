"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app    
    db.init_app(app)

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'

    def __repr__(self):
        c = self
        return f"<Cupcake: {c.id} flavor={c.flavor} size={c.size} rating={c.rating} image={c.image}"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String,
                       nullable=False)
    size = db.Column(db.String,
                     nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.String,
                      default='https://tinyurl.com/demo-cupcake')
    

    def serialize_cupcake(self):
        """Serialize a cupcake SQLAlchemy obj to dictionary"""
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image
        }