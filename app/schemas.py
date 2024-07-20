#  importing schema,fields,validate from marshmallow
from marshmallow import Schema, fields, validate
# Define a schema for Employee
class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)  # Integer  for employee ID
    name = fields.Str(required=True, validate=validate.Length(min=1))  # String  for employee name, required and minimum length is =1
    dept = fields.Str(required=True, validate=validate.Length(min=1))  # String for department, required and minimum length will be =1
    position = fields.Str(required=True, validate=validate.Length(min=1))  # String for position, required and minimum length is = 1
    salary = fields.Float(required=True)  # Float  for salary,

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)