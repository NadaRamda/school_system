from odoo import models, fields, api


class SchoolGrade(models.Model):
    _name = 'school.grade'
    _description = 'school.grade'


    grade_num =fields.Integer(String="Grade")
    count = fields.Integer(String="Number of Grades")



class SchoolStudents(models.Model):
        _name = 'school.students'
        _description = 'school.students'


        gender = fields.Char(string="Gender")
        class_num = fields.Many2one('school.class',string="Class")
        grade =fields.Char(related='class_num.grade')

class SchoolClass(models.Model):
        _name = 'school.class'
        _description = 'school.class'

        class_name=fields.Char("Class")
        grade = fields.Many2one('school.grade',string='Grade')



class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'school.subject'


    subject_name =fields.Char(string="Subject")
    subject =fields.Many2one('school.grade')






