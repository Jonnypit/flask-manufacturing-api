from flask import Blueprint, jsonify, request
from database import db
from models import Order

bp = Blueprint("orders", __name__)

@bp.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.__dict__ for o in orders])

@bp.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.__dict__)

@bp.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    new_order = Order(
       part_id=data["part_id"],
       quantity=data["quantity"],
       status=data["status"],
       date=data["date"]
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.__dict__), 201

@bp.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
       return jsonify({"error": "Order not found"}), 404
    data = request.get_json()
    order.part_id       = data["part_id"]
    order.quantity      = data["quantity"]
    order.status         = data["status"]
    order.date           = data["date"]
    db.session.commit()
    return jsonify(order.__dict__)

@bp.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order=Order.query.get(order_id)
    if order is None:
        return jsonify({"error": "Order not found"})
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": f"Order {order_id} deleted"})
