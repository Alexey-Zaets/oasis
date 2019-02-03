# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Test(models.Model):
    _name = 'test.test'

    test_name = fields.Char()
    test_purpose = fields.Text(translate=True)
    tester_id = fields.Many2one(
        'res.partner',
        ondelete='set null',
        index=True
        )

class TestSession(models.Model):
    _name = 'test.test_session'

    test_id = fields.Many2one(
        'test.test',
        ondelete='cascade',
        required=True
        )
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help='Duration in days')
    active = fields.Boolean(default=True)

    tester_id = fields.Many2many(
        'res.partner',
        srting='Tester',
        domain=[
            '|',
            ('tester', '=', True),
            ('category_id.name', 'ilike', 'Tester')
            ]
        )

    @api.depends('start_date')
    def _duration_value(self):
        pass
#    value = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100