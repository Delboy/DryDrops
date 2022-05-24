from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.


def view_contact_page(request):
    """ A view to return the contact page """
    # Uses message form to send email
    if request.method == 'POST':
        cust_name = request.POST.get('name')
        cust_email = request.POST.get('email')
        subject = request.POST.get('subject')
        subject = render_to_string(
            'contact/confirmation_emails/confirmation_email_subject.txt',
            {'subject': subject})
        message = request.POST.get('message')
        message = render_to_string(
            'contact/confirmation_emails/confirmation_email_body.txt',
            {'cust_name': cust_name, 'message': message}
        )
        # Sends confimation email to customer
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
        inbox_subject = request.POST.get('subject')
        inbox_subject = render_to_string(
            'contact/confirmation_emails/customer_service_email_subject.txt',
            {'inbox_subject': inbox_subject})
        inbox_message = request.POST.get('message')
        inbox_message = render_to_string(
            'contact/confirmation_emails/customer_service_email_body.txt',
            {
                'cust_name': cust_name,
                'inbox_message': inbox_message,
                'cust_email': cust_email
            }
        )
        # Sends message from user to dry drops inbox
        send_mail(
            inbox_subject,
            inbox_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )
        messages.success(
            request,
            f'Message successfully sent. \
                A confirmation email will be sent to {cust_email}.'
            )

    return render(request, 'contact/contact.html')
