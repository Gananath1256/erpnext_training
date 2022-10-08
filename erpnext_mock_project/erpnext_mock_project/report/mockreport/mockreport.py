
import frappe
from frappe import _

def execute(filters=None):
	conditions = get_conditions(filters)
	columns = get_columns()
	data = get_data(filters,conditions)
	return columns, data	
def get_columns():
	columns = [
		{
			"fieldname": "name",
			"label":_("Employee"),
			"fieldtype": "Data",
			# "options": "Sales Order",
			"width": 200
		},
		{
			"fieldname": "employee_name",
			"label": _("Full Name"),
			"fieldtype": "Data",					
			#"options": "Customer",
			"width": 200
		},
		{
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Select",
			"options":("Present"),
			"width": 200
		},
        {
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Select",
			"options":("Absent"),
			"width": 200
		},
        {
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Select",
			"options":("On Leave"),
			"width": 200
		},
        {
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Select",
			"options":("Half Day"),
			"width": 200
		},
		{
			"fieldname": "shift",
			"label": _("Shift"),
			"fieldtype": "Link",
			"options": ("Shift Type"),
			"width": 200	
		},
	
	]
	
	return columns

def get_data(filters,conditions):
	data=frappe.db.sql(f"""select e.name,
    a.status
    from `tabEmployee` as e left join `tabAttendence` as a on 
	
	'{filters.get('from_date')}' and '{filters.get('to_date')}' {conditions} """,as_dict=True)
	return data 

def get_conditions(filters):
	condition    = ""
	if filters.get('from_date'):
		conditions += " AND  transaction_date > '{}'".format(filters.get('from_date'))
	if filters.get('to_date'):
		conditions+= " AND transaction_date <'{}'".format(filters.get('to_date'))
	if filters.get('status'):
		conditions+= " AND employee = '{}'".format(filters.get('employee'))
	return conditions
	
	
