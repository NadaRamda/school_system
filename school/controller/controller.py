from odoo.addons.web.controllers import main as web
from odoo import http, _, exceptions
from odoo.http import request
import json


class OdooAPI(web.Home):
    @http.route(
        '/auth/',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        try:
            login = post["login"]
        except KeyError:
            raise exceptions.AccessDenied(message='`login` is required.')

        try:
            password = post["password"]
        except KeyError:
            raise exceptions.AccessDenied(message='`password` is required.')

        try:
            db = post["db"]
        except KeyError:
            raise exceptions.AccessDenied(message='`db` is required.')

        http.request.session.authenticate(db, login, password)
        res = request.env['ir.http'].session_info()
        return res

    @http.route('/api/post/createstudent/', auth='public', type='json', methods=['POST'])
    def create_student(self, **kw):
        kw = request.httprequest.get_data()
        kw = json.loads(kw)
        vals = {
            "gender" : kw.get('Gender'),
        }
        student = http.request.env['school.students'].sudo().create(vals)
        response = {"code": 200, "message": "Sucess", "ID": student.id}
        return response

