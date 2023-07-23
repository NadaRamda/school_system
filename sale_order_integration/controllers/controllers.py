# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request,  Response
import json


class Campany(http.Controller):
    @http.route('/api/post/createsaleorder/', auth='public', type='json', methods=['POST'])
    def create_saleorder(self, **kw):
        try:
            # access_token = request.httprequest.headers['Authorization']
            # if access_token != token:
            #     return {
            #         'message': 'No valid token ',
            #         'code': "401"
            #     }
            kw = request.httprequest.get_data()
            kw = json.loads(kw)
            # try:
            #     kw = json.loads(kw)
            #     required_value = ['CustomerCodeID', 'Lines']
            #     missing_value = self._check_required_values(data=kw, keys=required_value)
            #     if missing_value:
            #         return {
            #             'message': "missing parameters",
            #             'code': "404"
            #         }
            # except ValueError:
            #     return {
            #         'message': 'Invalid json data %r' % (request,),
            #         'code': 400
            #     }
            order = []
            list = []
            for line in kw.get('Lines'):
                product_id = request.env['product.product'].sudo().search([('id', '=', line.get('Product_id'))])
                if product_id:
                    list.append((0, 0, {
                        'product_id': product_id.id,
                        'price_unit': line.get('Price_unit'),
                        'name': line.get('Description'),
                        'product_uom_qty': line.get('Qty')
                    })
                                )
                else:
                    response = {'code': 401, 'message': "No valid Product_id = " + str(line.get('Product_id'))}
                    return response

            partner_id = request.env['res.partner'].search([('name', '=', kw.get('CustomerName'))])
            if not partner_id:
                partner_id = request.env['res.partner'].sudo().create({
                    "name": kw.get('CustomerName')
                })
            order.append({
                "partner_id": partner_id.id,
                "order_line": list,
            })
            orders = http.request.env['sale.order'].sudo().create(order)
            data = {
                'CustomerName': orders.display_name,
                'CustomerID': orders.id,
                'TotalAmount': orders.amount_total,
                'TaxedAmount': orders.amount_tax,
                'UntaxedAmount': orders.amount_untaxed,
            }
            response = {"code": 200, "message": "Everything worked as expected", "data": data}
            return response
        except Exception as e:
            response = {"code": 400, "message": str(e)}
            return response
