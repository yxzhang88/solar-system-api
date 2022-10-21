from flask import Blueprint, jsonify

class Planet:

    def __init__(self, id, name, description, temp):
        self.id = id
        self.name = name
        self.description = description
        self.temp = temp

planets = [Planet(1, "Earth", "Our world", 50), 
           Planet(2, "Mars", "hostile to life",-81), 
           Planet(3, "Venus", "Earth's sister", 900)]


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planet_response = []
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "temp": planet.temp
        }
        planet_response.append(planet_dict)
    return jsonify(planet_response), 200
