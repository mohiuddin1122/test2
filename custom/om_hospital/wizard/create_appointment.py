from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date', required=False)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
        }
        patient_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': patient_rec.id,
            'type': 'ir.actions.act_window',
            # for popup field
            'target': 'new',
        }

    def action_view_appointment(self):
        # when using self.env.ref you have to give ful id like om_hospital.hospital_appointment
        action = self.env.ref('om_hospital.hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.ids)]
        return action
