from odoo import models,fields

class Doctor(models.Model):
    _name= 'hospital.doctor'
    _description = 'Doctor'

    name= fields.Char(string='Name')
    specialization = fields.Selection([('Ortho', 'Ortho'),
                                    ('ENT', 'ENT'),], string='Specialization')
    phone_no = fields.Char(string='Phone Number')
    appointment_id = fields.One2many('hospital.appointment','doctor_id',string='Appointment')
