from rest_framework.decorators import api_view
from odoo.serializer.Serial import Serializers
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
        Users = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
        necessary = models.execute_kw(db, uid, password, 'res.partner', 'read', [Users])
        ser = Serializers(necessary, many=True)
        return Response(ser.data)

    elif request.method=='POST':

        ser= Serializers(data=request.data)
        uname = request.data['name']
        uvat = request.data['vat']
        ucity = request.data['city']
        uemail = request.data['email']
        ucompany_type= request.data['company_type']
        mobile = request.data['mobile']
        phone = request.data['phone']
        ref = request.data['ref']
        #property_payment_term_id = request.data['property_payment_term_id']



        models.execute_kw(db, uid, password, 'res.partner', 'create',
                         [{'name': uname, 'vat': uvat, 'city': ucity, 'email': uemail
                            ,'company_type':ucompany_type,'mobile':mobile,'phone':phone,'ref':ref}])

        return Response(status=status.HTTP_201_CREATED)

