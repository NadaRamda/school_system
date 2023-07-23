# -*- coding: utf-8 -*-

import json
import requests
from odoo import models, api

headers = {'content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'nada'}


class InheritSale(models.Model):
    _inherit = ['sale.order']

    def action_confirm(self):
        res = super(InheritSale, self).action_confirm()
        url = 'http://0.0.0.0:8014/api/post/createsaleorder'
        list = []
        for line in self.order_line:
            list.append({"Product_id": line.product_id.id,
                         "Price_unit": line.price_unit,
                         "Description": line.name,
                         "Qty": line.product_uom_qty})
        data = {"CustomerCodeID": self.id,
                "CustomerName": self.display_name,
                "Lines": list, }
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=headers)
        print(response.json())
        response.json()
        return res