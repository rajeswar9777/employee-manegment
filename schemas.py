# schemas.py

from marshmallow import Schema, fields

class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    department = fields.Str(required=True)
