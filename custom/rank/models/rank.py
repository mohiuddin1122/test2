from odoo import api, fields, models, _


class Rank(models.Model):
    _name = "hr.rank"
    # for chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hr Rank"
    _order = 'company_id asc'

    # generate sequence value for field
    company_id = fields.Many2one('res.company', string='Company Name', required=True)
    note = fields.Text(string='Description')
    name = fields.Char(string='Title')
    min_salary = fields.Integer(string='Min Salary')
    max_salary = fields.Integer(string='Max Salary')
