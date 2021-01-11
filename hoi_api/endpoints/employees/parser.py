from flask_restful import fields
from flask_restful import reqparse

domain_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'father_name': fields.String,
    'address': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'salary': fields.String,
}

employee_list_fields = {
    'count': fields.Integer,
    'employees': fields.List(fields.Nested(domain_fields)),
}

parser = reqparse.RequestParser()
parser.add_argument('first_name', type=str, required=True, location=['json'],
                    help='first_name parameter is required')
parser.add_argument('last_name', type=str, required=True, location=['json'],
                    help='last_name parameter is required')
parser.add_argument('father_name', type=str, required=True, location=['json'],
                    help='father_name parameter is required')
parser.add_argument('address', type=str, required=True, location=['json'],
                    help='address parameter is required')
parser.add_argument('email', type=str, required=True, location=['json'],
                    help='email parameter is required')
parser.add_argument('phone', type=str, required=True, location=['json'],
                    help='phone parameter is required')
parser.add_argument('salary', type=str, required=True, location=['json'],
                    help='salary parameter is required')
