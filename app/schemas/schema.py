from app import ma
from marshmallow import fields

class UserBasicSchema(ma.Schema):
    username = fields.String()

class UserAdminSchema(UserBasicSchema):
    id = fields.Integer(dump_only=True)
    password_hash = fields.String()
    hi_username= fields.Method('get.username')

    def get_username(self, obj):
        return f'hi {obj.username}'

class PaisSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre =fields.String()

class ProvinciaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre =fields.String()
    pais =fields.Integer()
    pais_obj=fields.Nested(
    PaisSchema, exclude=('id',))

class LocalidadSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre =fields.String()
    pais =fields.Integer()
    localidad = fields.Integer()
    pais_obj=fields.Nested(
    PaisSchema, exclude=('id',))
