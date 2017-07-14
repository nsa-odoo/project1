from datetime import datetime, timedelta

from odoo import api, fields, models, _

from openerp.exceptions import ValidationError


class emp_emp(models.Model):
    
    _name = 'employe.employe'
    
    _description = 'Employe'
    
    name = fields.Char('Name' , size = 20 ,required = True  )
    age = fields.Integer('Age' , default = 20)
    sal = fields.Float('Salary' , digit = (5,2))
    active = fields.Boolean('Active' , default = True)
    birthdate = fields.Datetime('BirthDate', readonly = True)
    join_date = fields.Date('Join Date')
    notes = fields.Text('Notes' , help = "this is used to write any text")
    template = fields.Html('Template')
    gender = fields.Selection([('male','Male'),('female','Female')],'Gender' , default = 'male')
    dept_id = fields.Many2one('emp.dept' , 'Department' )
    dept_code = fields.Char(related='dept_id.code',string='Dept Code')
    sal_ids = fields.One2many('emp.sal' , 'emp_id' , 'salary')
    activity_ids = fields.Many2many('emp.activity', string='Activity')
    pwd = fields.Char('Password')
    email = fields.Char('Email')
    website = fields.Char('Website')
    sign_in_time = fields.Float('Sign in Time')
    priority = fields.Selection([(str(i),str(i)) for i in range(6)],'Priority')
    partner_id = fields.Many2one('res.partner','Address')
    document = fields.Binary('Document')
    image = fields.Binary('Image')
    file_name = fields.Char('File Name')
    reference = fields.Reference(selection=[
                            ('res.partner','Partner'),
                            ('res.users','User'),
                            ('employee.employee','Employee')
                ], string='Reference')
    currency_id = fields.Many2one('res.currency','Currency')
    currency_rate = fields.Float(related="currency_id.rate", string="Currency Rate")
    bonus = fields.Monetary(currency_field='currency_id',string='Bonus')
    state = fields.Selection([('applied','Applied'),
                              ('interviewed','Interviewed'),
                              ('selected','Selected'),
                              ('rejected','Rejected'),
                              ('joined','Joined'),
                              ('notice_period','Notice'),
                              ('relieved','Relieved'),
                              ('terminated','Terminated')
                              ], string="State", default='applied')
    total_gross = fields.Float(compute='_calc_total_gross', string='Total Gross')
    total_net = fields.Float(compute='_calc_total_net', string='Total Net')
    percent = fields.Float(compute='_calc_percentage',string='Percentage')



    _sql_constraints = [
        ('unique_name','unique(name)','The name of the Employee must be unique!')
    ]
    

    print "okkkkkkkkkkkkkkkkkkkkkkkk"

    
    @api.constrains('age')
    def check_age(self):
        for emp in self:
            if emp.age < 18:
                raise ValidationError('You should be an adult to become an Employee!')




    @api.multi
    def _calc_total_gross(self):
        for emp in self:
            total = 0.0
            for sal in emp.sal_ids:
                total = total + sal.gross
            emp.total_gross = total
            
    @api.multi
    def _calc_total_net(self):
        for emp in self:
            total = 0.0
            for sal in emp.sal_ids:
                total = total +sal.net
            emp.total_net = total
    



    @api.multi
    def _calc_percentage(self):
        for emp in self:
            emp.percent = 0.0
            if emp.total_gross:
                emp.percent = emp.total_net * 100 / emp.total_gross
    



class emp_dept(models.Model):

    _name = 'emp.dept'

    _description = 'department'

    name = fields.Char('Name')
    code = fields.Char('code')

class emp_sal(models.Model):

    _name = 'emp.sal'
    _description = 'salary'



    @api.depends('basic','allowances')
    def _calc_gross(self):
        for sal in self:
            sal.gross = sal.basic + sal.allowances
        
    @api.depends('gross','deductions')
    def _calc_net(self):
        print "SasdafdsdfELF",self
        for sal in self:
            sal.net = sal.gross - sal.deductions
    

    month = fields.Char('Month')
    basic = fields.Float('Basic')
    allowances = fields.Float('Allowances')
    deductions = fields.Float('Deductions')
    gross = fields.Float(compute='_calc_gross',string='Gross', store=True)
    net = fields.Float(compute='_calc_net',string='Net', store=True)
    emp_id =  fields.Many2one('employe.employe','Employe')

class emp_activity(models.Model):
    
    _name = 'emp.activity'
    
    name = fields.Char('Name')
    code = fields.Char('Code', size=4)