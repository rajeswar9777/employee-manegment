from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to Employee Management System"})

if __name__ == '__main__':
    app.run(debug=True)

employees = []

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((emp for emp in employees if emp['id'] == id), None)
    return jsonify(employee) if employee else ('', 404)

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = next((emp for emp in employees if emp['id'] == id), None)
    if employee:
        data = request.get_json()
        employee.update(data)
        return jsonify(employee)
    return ('', 404)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employees = [emp for emp in employees if emp['id'] != id]
    return ('', 204)

from models import db, Employee

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([emp.to_dict() for emp in employees])

@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], age=data['age'], department=data['department'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.to_dict()), 201

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.to_dict())

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.get_json()
    employee.name = data['name']
    employee.age = data['age']
    employee.department = data['department']
    db.session.commit()
    return jsonify(employee.to_dict())

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return ('', 204)
