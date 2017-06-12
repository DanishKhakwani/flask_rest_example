from flask_app.app import db

class Animal(db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(100))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color
        }

