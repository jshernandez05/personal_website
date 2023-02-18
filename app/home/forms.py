from django import forms
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=120)
    email = forms.EmailField(required=True, max_length=150)
    subject = forms.CharField(required=True, max_length=500)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=2500)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\nSubject:  {subject}\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()
        send_mail(
            subject=f'New contact message from jshernandez05.com: {subject}',
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
