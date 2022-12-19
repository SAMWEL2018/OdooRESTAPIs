import xmlrpc.client
from rest_framework import status
from rest_framework.decorators import api_view

from odoo.serializer.Serial import payment_method_specific
from rest_framework.response import Response


url = "http://localhost:8069"
db = "oyake_softiq"  # database name here
username = 'odoo@softiqtechnologies.co.ke'
password = "admin4321"
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


@api_view(['GET','POST'])
def payment_item(request,id):

    if request.method=='GET':
        pos = models.execute_kw(db, uid, password, 'pos.payment', 'search', [[['id', '=', id]]])
        necessary = models.execute_kw(db, uid, password, 'pos.payment', 'read', [pos])
        ser = payment_method_specific(necessary, many=True)
        print(ser.data)
        return Response(ser.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

