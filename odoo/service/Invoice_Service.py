import json


class PostInvoice:
    def __init__(self):
        self.amount = 0
        self.name = ""
        self.amountIncludingVAT=""
        self.billToName = ""
        self.sellToCustomerName=""
        self.documentDate = ""
        self.postingDate = ""
        self.pricesIncludingVAT= True
        self.customerPostingGroup = "DOMESTIC"
        self.product_name=""
        self.qty = ""
        self.price_unit = ""
        self.unit_measure=""


    def getJson(self):
        return json.dumps(self.__dict__)

print(PostInvoice().getJson())



