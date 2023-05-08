from datetime import date
from odoo import fields, models, api


class ProjectAssignment(models.Model):
    _name = "project.assignment"
    _description = "project Assignment"
    _rec_name = 'project_name'

    project_name = fields.Many2one(comodel_name='project.project', string='project Name', required=True)
    employees_list_ids = fields.One2many('employees.list', 'project_id', string='Employees')
