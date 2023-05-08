from odoo import fields, models


class EmployeesList(models.Model):
    _name = "employees.list"
    _description = "Employees List "

    employee_id = fields.Many2one('hr.employee', required=True)
    # weighting = fields.Integer(string='Weighting', default="1")
    weighting = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')], default='1', string="weighting")
    project_id = fields.Many2one('project.assignment', string='project ID')
