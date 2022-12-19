from flask import Response

from odoo.inventory_adjustments import db, uid, password, models
from odoo.serializer.Serial import payment_method_serializer


def payment(request):

        pos = models.execute_kw(db, uid, password, 'pos.payment', 'search', [[]])
        necessary = models.execute_kw(db, uid, password, 'pos.payment', 'read', [pos])
        ser = payment_method_serializer(necessary, many=True)
        return Response(ser.data)
