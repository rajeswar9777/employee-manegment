# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from schemas import EmployeeSchema

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

@app.route('/employees', methods=['POST'])
def create_employee():
    try:
        data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    
    return employee_schema.jsonify(new_employee), 201

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return employee_schema.jsonify(employee)

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return employees_schema.jsonify(employees)

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    try:
        data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    employee.name = data['name']
    employee.age = data['age']
    employee.department = data['department']
    db.session.commit()

    return employee_schema.jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
