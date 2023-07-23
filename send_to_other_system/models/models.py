from odoo import models, api
import json
import requests

# headers = {'content-type': 'application/json', 'Accept': 'application/json'}
#
# class ResPartnerInherit(models.Model):
#     _inherit = 'res.partner'
#
#
#     @api.model
#     def create(self, vals):
#         rec = super(ResPartnerInherit, self).create(vals)
#         print(rec)
#         self.send_data_to_other({'name': rec.name, 'email': rec.email, 'phone': rec.phone})
#         return rec
#
#
#     def send_data_to_other(self,data):
#         url ='http://localhost:8014'
#         db ='new'
#         username ='n'
#         password ='n'
#
#         # db = 'db_2'
#         # username = 'odoo'
#         # password = 'odoo'
#
#         athenticated =self.athen_with_db(url, db, username, password)
#         if athenticated :
#             url += '/api/post/createstudent/'
#             payload = {
#                 "params": {
#                     "args": [],
#                     "kwargs": data,}
#                 }
#             payload = json.dumps(payload)
#             response = requests.post(url=url, data=payload, headers=headers)
#             # response = response.json()
#             return response.text
#
#     def athen_with_db (self,url,db,username,password):
#         url += '/auth/'
#         payload = {"params": {"login": username , "password": password,
#                               "db": db}}
#         payload = json.dumps(payload)
#         response = requests.post(url=url, data=payload, headers=headers)
#
#         response = response.json()
#         # cookies = response.cookies
#         # print("response", cookies)
#         # return {'cookies': cookies}




import logging

LOGGER = logging.getLogger(__name__)


class res_partner_inherit(models.Model):
    _inherit = 'res.partner'

    def send_student_to_other_system(self, student_data):
        #
        url = 'http://localhost:8014'

        db = 'new'
        username ='n'
        password ='n'

        # auth with db
        authenticated = self.auth_with_db(url, username, password, db)
        if authenticated:
            url = url + "/object/res.partner/create_student"

            payload = {
                "params": {
                    "args": [],
                    "kwargs":  student_data

                }

            }
            payload = json.dumps(payload)
            headers = {
                'content-type': "application/json",

            }

            response = requests.request("POST", url, data=payload, headers=headers, cookies=authenticated['cookies'])

            # print("result response :> ", response.text)

    def auth_with_db(self, url, username, password, db_name):
        #
        url += "/auth"
        payload = {"params": {"login": username, "password": password,
                              "db": db_name}}

        payload = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            # 'cache-control': "no-cache",
            # 'postman-token': "1c96a08b-f55e-d2b0-b63c-a4eb9b412e74"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        cookies = response.cookies
        if response.status_code == 200:
            response = json.loads(response.text)
            if "result" in response and response['result']['uid'] > 0:
                return {'cookies': cookies}
            else:
                return False
        else:
            return False

    @api.model
    def create(self, vals):
        record = super(res_partner_inherit, self).create(vals)

        # send student data to other systems
        self.send_student_to_other_system({'name': record.name, 'email': record.email, 'phone': record.phone})

        return record

