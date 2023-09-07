from django import forms
from django.forms import ModelForm


# class EmployeeForm(ModelForm):
#     class Meta:
#         model = Employee
#         fields = "__all__"


class EmployeeForm(forms.Form):
    name = forms.CharField(label="Enter name",max_length=20)
    age = forms.IntegerField(label="Enter age")
    email = forms.EmailField(label="Enter Your Email")
    address = forms.CharField(widget=forms.Textarea)