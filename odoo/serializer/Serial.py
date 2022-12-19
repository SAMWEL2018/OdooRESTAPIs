from rest_framework import serializers
from odoo.model.models import comments,products,pointofsale,purchase_order,inventory_adjustments,order_line,payment_method,payment_method_specific


class Serializers(serializers.ModelSerializer):
    class Meta:
        model= comments
        #fields= '__all__'
        fields = '__all__'
        #fields=['name','vat','city','email','company_type']


class product_serializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

class purchase_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = purchase_order
        fields = '__all__'

class pos_serializer(serializers.ModelSerializer):
    class Meta:
        model = pointofsale
        fields = '__all__'

class adjustments_serializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_adjustments
        fields = '__all__'

class order_line_serializer(serializers.ModelSerializer):
    class Meta:
        model = order_line
        fields = '__all__'

class payment_method_serializer(serializers.ModelSerializer):
    class Meta:
        model = payment_method
        fields = '__all__'

class payment_method_specific(serializers.ModelSerializer):
    class Meta:
        model = payment_method_specific
        fields = '__all__'