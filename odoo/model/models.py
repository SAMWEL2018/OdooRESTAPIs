from django.db import models

class comments(models.Model):
    name= models.CharField(max_length=100)
    display_name= models.CharField(max_length=100)
    vat=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_type= models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    property_product_pricelist = models.CharField(max_length=100)
    #is_sent = models.CharField(max_length=100)
    #property_payment_term_id = models.CharField(max_length=100)



class products(models.Model):
    name= models.CharField(max_length=100)
    list_price= models.CharField(max_length=100)
    standard_price= models.CharField(max_length=100)
    create_date= models.CharField(max_length=100)
    write_uid= models.CharField(max_length=100)
    default_code = models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    property_account_income_id= models.CharField(max_length=100)
    property_account_expense_id= models.CharField(max_length=100)
    detailed_type = models.CharField(max_length=100)
    invoice_policy= models.CharField(max_length=100)
    uom_id=models.CharField(max_length=100)
    uom_po_id=models.CharField(max_length=100)
    taxes_id=models.CharField(max_length=100)
    categ_id= models.CharField(max_length=100)
    available_in_pos= models.CharField(max_length=100)
    pos_categ_id= models.CharField(max_length=100)
    sale_ok= models.CharField(max_length=100)
    purchase_ok= models.CharField(max_length=100)
    qty_available =  models.CharField(max_length=100)



class purchase_order(models.Model):
    name= models.CharField(max_length=100)
    partner_id= models.CharField(max_length=100)
    partner_ref=models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    date_order = models.CharField(max_length=100)
    date_approve = models.CharField(max_length=100)
    picking_type_id = models.CharField(max_length=100)
    invoice_status= models.CharField(max_length=100)
    amount_untaxed = models.CharField(max_length=100)
    tax_totals_json = models.CharField(max_length=500)

class pointofsale(models.Model):
    name= models.CharField(max_length=100)
    #session_id = models.CharField(max_length=100)
    date_order = models.CharField(max_length=100)
    pos_reference = models.CharField(max_length=100)
    partner_id = models.CharField(max_length=100)
    #employee_id = models.CharField(max_length=100)
    amount_total = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    margin = models.CharField(max_length=100)
    lines = models.CharField(max_length=1000)

class inventory_adjustments(models.Model):
    location_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    product_uom_id = models.CharField(max_length=100)
    inventory_quantity = models.CharField(max_length=100)
    inventory_date = models.CharField(max_length=100)

class order_line(models.Model):
    full_product_name = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price_unit= models.CharField(max_length=100)
    discount = models.CharField(max_length=100)

class payment_method(models.Model):
    payment_date = models.CharField(max_length=100)
    payment_method_id = models.CharField(max_length=100)
    pos_order_id = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

class payment_method_specific(models.Model):
    amount = models.CharField(max_length=100)
    payment_method_id = models.CharField(max_length=100)
    pos_order_id = models.CharField(max_length=100)



