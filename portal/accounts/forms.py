from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import About , Student ,Field_name_list
from bootstrap_datepicker.widgets import DatePicker
# class UserCreateForm(UserCreationForm):
#     class Meta:
#         fields = ("username", "email", "first_name", "last_name" ,  "password1" )
#         model = get_user_model()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].label = "Display name"
#         self.fields["email"].label = "Webmail"
#         self.fields["first_name"].label = "First name"
#         self.fields["last_name"].label = "Last name"


class Login_Form(forms.ModelForm):
    MODE_CHOICE = (
        ( 0 , 'Student'),
        ( 1 , 'Admin'),
    )
    mode = forms.TypedChoiceField(choices=MODE_CHOICE, widget=forms.RadioSelect, coerce=int)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = About
        fields = ('username','password' , 'mode')

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class Student_Request_Form(forms.ModelForm):
    Field_name = forms.CharField(max_length=60,widget=forms.Select(choices= Field_name_list) , required=True)
    class Meta:
        model = Student
        fields = ('Field_name','purpose' , 'Booking_date' , 'Booking_time' )
        widgets = {
            'Booking_date': DateInput(),
            'Booking_time': TimeInput(),
        }
