from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                             string="Status", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    # generate sequence value for field
    reference = fields.Char(string='Sequence', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    # define a function for confirm button
    def action_confirm(self):
        # change state
        self.state = 'confirm'

    # define a function for done button
    def action_done(self):
        self.state = 'done'

    # define a function for draft button
    def action_draft(self):
        self.state = 'draft'

    # define a function for cancel button
    def action_cancel(self):
        self.state = 'cancel'

    # How to set or override the create method

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        if not res.get('gender'):
            res['gender'] = 'female'
        return res
