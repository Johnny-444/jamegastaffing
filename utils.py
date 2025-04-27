import os
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification_email(subject, body_text):
    """
    Send notification email to staff when a form is submitted
    """
    # Get email configuration from environment variables
    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    sender_email = os.environ.get('NOTIFICATION_EMAIL', 'notifications@jamegastaffing.com')
    sender_password = os.environ.get('EMAIL_PASSWORD', '')
    recipient_email = os.environ.get('STAFF_EMAIL', 'staff@jamegastaffing.com')
    
    # If email credentials are not set, just log the notification
    if not sender_password:
        logging.info(f"Email would be sent: {subject} - {body_text}")
        return
    
    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Attach body
        message.attach(MIMEText(body_text, 'plain'))
        
        # Connect to server and send
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            
        logging.info(f"Notification email sent: {subject}")
        
    except Exception as e:
        logging.error(f"Failed to send notification email: {e}")
