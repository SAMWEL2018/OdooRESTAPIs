from rest_framework.decorators import api_view
from odoo.serializer.Serial import adjustments_serializer
import xmlrpc.client
from rest_framework import status

from rest_framework.response import Response


url = "http://localhost:8069"
db = "OYAKEDB"  # database name here
username = 'bochere@oyake.co.ke'
password = "Uwezo@!"
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

@api_view(['GET','POST','PUT'])
def index(request):

    if request.method=='GET':
        products = models.execute_kw(db, uid, password, 'stock.quant', 'search', [[]])
        necessary = models.execute_kw(db, uid, password, 'stock.quant', 'read', [products])
        ser = adjustments_serializer(necessary, many=True)
        return Response(ser.data)

    elif request.method=='PUT':

        id = request.data['id']
        stock = request.data['inventory_quantity']
        print('ID',id)
        print('STOCK', stock)

        products = models.execute_kw(db, uid, password, 'stock.quant', 'search', [[['id', '=', id]]])
        necessary = models.execute_kw(db, uid, password, 'stock.quant', 'read', products)
        data = necessary[0]

        quantity = data['available_quantity']
        print(quantity)
        stock = sum(quantity,stock)

        models.execute_kw(db, uid, password, 'stock.quant', 'write',[[id],{'quantity': stock}])
        res = {"msg","DATA UPDATED"}
        return Response(status=status.HTTP_201_CREATED)


def sum(x,y):
    return float(x)+int(y)