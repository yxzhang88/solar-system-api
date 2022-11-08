
from flask import jsonify,abort,make_response

def validate_one_obj_or_abort(cls,obj_id):
    try:
        obj_id = int(obj_id)
    except:
        abort(make_response({"message": f"Planet {obj_id} invalid"}, 400))

    matching_obj =cls.query.get(obj_id)

    if not matching_obj:
        abort(make_response({"message": f"Planet {obj_id} not found"}, 404))
    
    return matching_obj