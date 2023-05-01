from odoo import fields, models


class EstateProperty(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient "
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', traking=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', traking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', traking=True)
    active = fields.Boolean(string='Active', default=True)
