from celery import shared_task
from utility.logger import appLogs 
from django.core.mail import send_mail
import smtplib

app = ""

def notification(subject, body, discount_code, client_name,  operator_first_name="Rosemary", dest_email="tipalov351@bomoads.com"):
    sender_email = "emenqfox@gmail.com"

    try:
        send_mail( 
                    "RE:" + subject,
                    "Hi "+ client_name + ',\n\n' + 
                    body + ',\n\n' + 
                    "You could also use our discount code, " +   discount_code  + ", for very good discounts" + ',\n\n\n\n' + 
                    "Best," + '\n\n' + 
                    operator_first_name,
                    sender_email,
                    [dest_email],
                    auth_user=sender_email,
                    auth_password = config('EMAIL_PASS'),
                    fail_silently=False
                    )

    except smtplib.SMTPException as e:
                appLogs('Error in mail sending: ', e)




