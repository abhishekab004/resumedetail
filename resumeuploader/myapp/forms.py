from django import forms
from myapp.models import Resume

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)

JOB_CITY_CHOICES =(
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Hyderabad','Hyderabad'),
    ('Lucknow','Lucknow'),
    ('Noida','Noida'),
    ('Dubai','Dubai')
)

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred Job Location',choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields='__all__'
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile Number','email':'Email ID','profile_image':'Profile Image','my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),

        }