from odoo import fields, models


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "appointment pharmacy lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(String="Quantity", default="1")
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
