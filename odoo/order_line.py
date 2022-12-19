import json
import xmlrpc.client

import requests
from rest_framework import status
from rest_framework.decorators import api_view

from odoo.serializer.Serial import order_line_serializer
from rest_framework.response import Response


url = "http://localhost:8069"
db = "oyake_softiq"  # database name here
username = 'odoo@softiqtechnologies.co.ke'
password = "admin4321"
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


@api_view(['GET','POST'])
def pos_line(request,id):

    if request.method=='GET':
        pos = models.execute_kw(db, uid, password, 'pos.order.line', 'search', [[['order_id', '=', id]]])
        necessary = models.execute_kw(db, uid, password, 'pos.order.line', 'read', [pos])
        ser = order_line_serializer(necessary, many=True)
        bulk =  json.dumps(ser.data)
        print(bulk)
        res = json.loads(bulk)
        print("res ",res)
        print(res[0]['qty'])
        return Response(ser.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

