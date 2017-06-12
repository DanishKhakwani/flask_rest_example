from flask import request
from flask_restful import reqparse, Resource

from flask_app.app import api, db
from flask_app.models import Animal


class AnimalResource(Resource):

    def get(self, animal_id):
        animal = db.session.query(Animal).filter_by(id=animal_id).first()
        if not animal:
            return {'message': 'Not Found'}, 404
        return animal.serialize

    def put(self, animal_id):
        animal = db.session.query(Animal).filter_by(id=animal_id).first()
        if 'name' in request.form:
            animal.name = request.form['name']
        if 'color' in request.form:
            animal.color = request.form['color']
        db.session.commit()
        return animal.serialize


class AnimalsListResource(Resource):

    def get(self):
        return [
                {animal.id: {'name': animal.name, 'color': animal.color}}
                for animal in db.session.query(Animal).all()
                ]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('color', required=True)
        args = parser.parse_args()

        new_animal = Animal(name=args['name'], color=args['color'])
        db.session.add(new_animal)
        db.session.commit()

        return {
            new_animal.id: {'name': new_animal.name, 'color': new_animal.color}
                }, 201

api.add_resource(AnimalResource, '/animal/<animal_id>')
api.add_resource(AnimalsListResource, '/animals')
