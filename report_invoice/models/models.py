from odoo import models, api


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def generate_report(self):
        return self.env.ref('report_invoice.invoive_report_pdf').report_action(self)
