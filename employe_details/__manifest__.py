{
    'name' : 'employee',
    'version' : '1',
    'description': "details of employee",
    'category': 'Employee',
    'website': 'https://www.odoo.com',
    'depends' : ['base' , 'report'],
    'data': [
        'security/emp_security.xml',
        'security/ir.model.access.csv',
        'views/employe_view.xml',
        'views/emp_report.xml',
        'views/hr_report.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


# acess_employe_hr_manager,acess.employe_hr_manager,model_employe_employe,grp_hr_mngr,1,1,1,1
# acess_employe_rpt_mngr,acess.employe_rpt_mngr,model_employe_employe,grp_rpt_mngr,1,1,0,0
# acess_employe_emp,acess.employe_emp,model_employe_employe,grp_hr_emp,1,0,0,0

