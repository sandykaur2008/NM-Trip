from app import sg
from sendgrid.helpers.mail import Email, Content, Mail

def send_email(subject, sender, recipient, text_body):
    from_email = Email(sender)
    to_email = Email(recipient)
    content = Content("text/plain", text_body)
    mail = Mail(from_email, subject, to_email, content)
    reponse = sg.client.mail.send.post(request_body=mail.get())