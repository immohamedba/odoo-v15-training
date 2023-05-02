from datetime import date
from odoo import fields, models, api


class EstateProperty(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient "
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', traking=True)
    ref = fields.Char(string='Reference')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute="_compute_age", traking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', traking=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('date_of_birth')
    def _compute_age(self):

        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
