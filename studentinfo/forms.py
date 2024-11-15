from django import forms
from .models import stud
class studForm(forms.ModelForm):
    # s_name  = forms.CharField(max_length=30)
    # s_course  = forms.CharField(max_length=30)
    # s_branch = forms.CharField(max_length=30)

    # s_college = forms.CharField(max_length=30)
    # s_email = forms.EmailField(max_length=30)
    class Meta:
        model = stud
        fields='__all__'


class SForm(forms.Form):
    s_roll = forms.IntegerField()
