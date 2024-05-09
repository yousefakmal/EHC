from django import forms
from .models import *
from datetime import date

class LogInForm(forms.Form):
    username = forms.CharField(
        label=False,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label=False,
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )



class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'ticket', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'Ticket_name'}),
            'ticket': forms.TextInput(attrs={'placeholder': 'Ticket', 'class': 'Ticket'}),
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'password', 'email', 'PhoneNumber')
    username = forms.CharField(
        label=False,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label=False,
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    email = forms.EmailField(
        label=False,
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    PhoneNumber = forms.CharField(
        label=False,
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['username', 'email', 'phone', 'feedback']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'feedback': forms.TextInput(attrs={'class':'bigbox','placeholder': 'Feedback'}),
        }
        labels = {
            'username': '',
            'email': '',
            'phone': '',
            'feedback': '',
        }
    

class MessageForm(forms.Form):
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Write your message'}))