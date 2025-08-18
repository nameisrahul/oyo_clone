from django.core.mail import send_mail
from django.conf import settings




import uuid


def generateRandomToken():
    return str(uuid.uuid4())




def sendEmailToken(email , token):
    subject = "Verify Your Email Address"
    message = f"""Hi Please verify you email account by clicking this link 
    http://127.0.0.1:8000/account/verify-account/{token}
    
    """
    send_mail(
       subject,
       message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


#utils.py

def sendOTPtoEmail(email , otp):
    subject = "OTP for Account Login"
    message = f"""Hi, use this OTP to login
     {otp} 
    
    """
    send_mail(
       subject,
       message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    #utils.py
from django.utils.text import slugify
from .models import Hotel

def generateSlug(hotel_name):
    slug = f"{slugify(hotel_name)}-" + str(uuid.uuid4()).split('-')[0]
    if Hotel.objects.filter(hotel_slug = slug).exists():
        return generateSlug(hotel_name)
    return slug
  
  #other functions