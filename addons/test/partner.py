from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    istester = fields.Boolean('isTester', default=False)

    session_ids = field.Many2many('test.test_session', readonly=True)