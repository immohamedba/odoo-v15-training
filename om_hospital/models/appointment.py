from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string="Patient")
    gender = fields.Selection(related="patient_id.gender", readonly=False)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help="Reference from patient record")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], bstring="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', bstring="Status", required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button clicked !!!!!!! ")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': ' Click succesfull',
                'type': 'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_in_done(self):
        for rec in self:
            rec.state = 'done'

    def action_in_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_in_draft(self):
        for rec in self:
            rec.state = 'draft'
