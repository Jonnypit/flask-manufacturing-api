from flask import Blueprint, jsonify, request
from database import db
from models import Part

bp = Blueprint("parts", __name__)

@bp.route("/parts", methods=["GET"])
def get_parts():
    parts = Part.query.all()
    return jsonify([p.to_dict() for p in parts])

@bp.route("/parts/<int:part_id>", methods=["GET"])
def get_part(part_id):
    part = Part.query.get(part_id)
    if part is None:
        return jsonify({"error": "Part not found"}), 404
    return jsonify(part.to_dict())

@bp.route("/parts", methods=["POST"])
def create_part():
    data = request.get_json()
    new_part = Part(
        name=data["name"],
        material=data["material"],
        quantity=data["quantity"],
        price=data["price"]
    )
    db.session.add(new_part)
    db.session.commit()
    return jsonify(new_part.to_dict()), 201

@bp.route("/parts/<int:part_id>", methods=["PUT"])
def update_part(part_id):
    part = Part.query.get(part_id)
    if part is None:
        return jsonify({"error": "Part not found"}), 404
    data = request.get_json()
    part.name       = data["name"]
    part.material   = data["material"]
    part.quantity   = data["quantity"]
    part.price      = data["price"]
    db.session.commit()
    return jsonify(part.to_dict())

@bp.route("/parts/<int:part_id>", methods=["DELETE"])
def delete_part(part_id):
    part =Part.query.get(part_id)
    if part is None:
        return jsonify({"error": "Part not found"}), 404
    db.session.delete(part)
    db.session.commit()
    return jsonify({"message": f"Part {part_id} deleted"})
    
                        




