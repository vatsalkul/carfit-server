from flask_restplus import Api

from .visits import api as ns1




api = Api(
    title='CarFit',
    version='0.1.0',
    description='',
)

api.add_namespace(ns1)

