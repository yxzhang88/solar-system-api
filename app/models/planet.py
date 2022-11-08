from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    temp = db.Column(db.Integer)


    @classmethod
    def from_dict(cls,data_dict):
        if "name" in data_dict and "description" in data_dict and "temp" in data_dict:
            new_obj = cls(name = data_dict["name"], description=data_dict["description"], temp=data_dict["temp" ] )
            return new_obj