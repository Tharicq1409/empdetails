from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ('fullname','emp_id','mail_id','position')
        lables = {
            'fullname' : 'Employee Name',
            'emp_id' : 'Employee ID',
            'mail_id' : 'Mail ID',
            'position' : 'Designation'
        }
        
   #this function is  
    def __init__(self,*args,**kwagrs):
        super(EmployeeForm,self).__init__(*args,**kwagrs)
        self.fields['position'].empty_label = "Select"
        self.fields['mail_id'].required = False # Making the field to be unrequired
        