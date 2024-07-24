from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<Employee {self.name}>'
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'department': self.department
        }
