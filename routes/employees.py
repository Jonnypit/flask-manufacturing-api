from flask import Blueprint, jsonify, request
from database import db
from models import Employee

bp = Blueprint("employees", __name__)

@bp.route("/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    return jsonify([e.to_dict() for e in employees])

@bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee.to_dict())

@bp.route("/employees", methods=["POST"])
def create_employee():
    data =request.get_json()
    new_employee = Employee(
        name=data["name"],
        role=data["role"],
        department=data["department"],
        hire_date=data["hire_date"]
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.to_dict()), 201

@bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    data =  request.get_json()
    employee.name       = data["name"]
    employee.role       = data["role"]
    employee.department = data["department"]
    employee.hire_date  = data["hire_date"]
    db.session.commit()
    return jsonify(employee.to_dict())

@bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    employee =Employee.query.get(employee_id)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": f"Employee {employee_id} deleted"})
