from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "this is description of my estate"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
       string='Type',
       selection=[('N', 'North'), ('E', 'East'), ('W', 'West'), ('S', 'South')],
       help="this is help Text")

