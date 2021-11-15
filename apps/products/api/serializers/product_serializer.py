
from apps.products.models import Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date')


    #Esto representa los valores reales en la vista y no solo los valores el id
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'name': instance.name,
            'description' : instance.description,
            'image': instance.image if instance.image != instance.image else '', #Se hace la validacion por que produce un erro de unicode ('utf-8' codec can't decode byte 0x89 in position 0: invalid start byte) por la imagen precargada. recondar que en el modelo no tiene activado el null
            'measure_unit': instance.measure_unit.description, #Es el campo que tiene el nombre en el modelo foreing key
            'category_product': instance.category_product.description
        }