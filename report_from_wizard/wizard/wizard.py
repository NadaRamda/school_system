from odoo import models, fields, api

class ContractReportWizard(models.TransientModel):
    _name = 'contract.report.wizard'
    _description = 'contract.report.wizard'


    date = fields.Date(String="Date", required=True)

    def generate_report_pdf (self):
        data = {
            "date": self.date,
        }
        return self.env.ref('report_from_wizard.report_pdf_wiz_contract').report_action(self, data=data)

    class ReportPdfcontract(models.AbstractModel):
        _name = 'report.report_from_wizard.report_contract'
        _description = 'stock report'

        @api.model
        def _get_report_values(self, docids, data=None):
            domain = [('date_start', '<=', data['date']), ('state', '=', 'open')]
            employees = self.env['hr.contract.history'].search(domain)
            tests = self.env['hr.contract.history'].search_read(domain)
            print(tests)
            return {
                'employees': employees,
                'data': data,
            }
