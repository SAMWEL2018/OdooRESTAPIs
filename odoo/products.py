from rest_framework.decorators import api_view
from odoo.serializer.Serial import product_serializers
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


@api_view(['GET','POST'])
def index(request):

    if request.method=='GET':
        products = models.execute_kw(db, uid, password, 'product.template', 'search', [[]])
        necessary = models.execute_kw(db, uid, password, 'product.template', 'read', [products])
        ser = product_serializers(necessary, many=True)
        return Response(ser.data)

    elif request.method=='POST':

        name = request.data['name']
        list_price= request.data['list_price']
        standard_price = request.data['standard_price']
        create_date = request.data['create_date']
        #write_uid= request.data['write_uid']
        default_code= request.data['default_code']
        detailed_type= request.data['detailed_type']
        invoice_policy= request.data['invoice_policy']
        available_in_pos = request.data['available_in_pos']
        sale_ok = request.data['sale_ok']
        purchase_ok = request.data['purchase_ok']
        #property_account_income_id= request.data['property_account_income_id']
        #property_account_expense_id= request.data['property_account_expense_id']


        models.execute_kw(db, uid, password, 'product.template', 'create',
                         [{'name': name, 'list_price': list_price, 'standard_price': standard_price,
                           'create_date': create_date,'default_code': default_code
                           ,'detailed_type':detailed_type,'invoice_policy':invoice_policy,'available_in_pos':available_in_pos,
                           'sale_ok':sale_ok,'purchase_ok':purchase_ok}])

        return Response(status=status.HTTP_201_CREATED)