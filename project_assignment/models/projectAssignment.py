from datetime import date
from odoo import fields, models, api


class ProjectAssignment(models.Model):
    _name = "project.assignment"
    _description = "project Assignment"
    _rec_name = 'project_name'

    project_name = fields.Many2one(comodel_name='project.project', string='project Name', required=True)
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
    employees_list_ids = fields.Many2many('hr.employee',  string='Employees')
