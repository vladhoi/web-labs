from flask_restful import Resource, request
from flask_restful import marshal_with, marshal

from app import db
from .model import Employee
from .parser import domain_fields, employee_list_fields, parser


class EmployeeResource(Resource):

    def get(self, employee_id=None):
        if employee_id:
            user = Employee.query.filter_by(id=employee_id).first()
            return marshal(user, domain_fields)
        else:
            args = request.args.to_dict()

            user = Employee.query.filter_by(**args).order_by(Employee.id)
            user = user.all()

            return marshal({
                'count': len(user),
                'employees': [marshal(u, domain_fields) for u in user]
            }, employee_list_fields)

    @marshal_with(domain_fields)
    def post(self):
        args = parser.parse_args()

        employee = Employee(**args)
        db.session.add(employee)
        db.session.commit()

        return employee

    @marshal_with(domain_fields)
    def put(self, employee_id=None):
        employee = Employee.query.get(employee_id)

        employee.first_name = request.json['first_name']
        employee.last_name = request.json['last_name']
        employee.father_name = request.json['father_name']
        employee.address = request.json['address']
        employee.phone = request.json['phone']
        employee.salary = request.json['salary']

        db.session.commit()
        return employee

    @marshal_with(domain_fields)
    def delete(self, employee_id=None):
        employee = Employee.query.get(employee_id)

        db.session.delete(employee)
        db.session.commit()

        return employee
