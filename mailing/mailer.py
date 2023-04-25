import smtplib
from email.message import EmailMessage

MY_EMAIL = input("Enter sender email address: ")
MY_PASSWORD = input("Enter sender password or application password: ")

TARGET_EMAIL = input("Enter recipient(s) email address: ")

with open("mailing/mail.html", "r") as mail_file:
    html_body = mail_file.read()

with open("mailing/mail.txt", "r") as mail_file:
    text_body = mail_file.read()


msg = EmailMessage()
msg["Subject"] = "Student Survey: Effects of Strike"
msg["From"] = MY_EMAIL
msg["To"] = TARGET_EMAIL
msg.set_content(text_body)
msg.add_alternative(html_body, subtype="html")


def send_email(port):
    try:
        if port == 587:
            connection = smtplib.SMTP("smtp.gmail.com", port)
            connection.ehlo()
            connection.starttls()
        elif port == 465:
            connection = smtplib.SMTP_SSL("smtp.gmail.com", port)

        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)
        connection.close()
        print(f"Port {port}: Successfully sent the mail! Check!")
    except smtplib.SMTPAuthenticationError:
        print(
            f"Port {port}: Failed to send email. Either a wrong password/email combination or your account may have 2-Factor Authentication enabled. You need to remove or create an application password instead. Learn more at https://support.google.com/mail/?p=InvalidSecondFactor"
        )


try:
    send_email(587)

except smtplib.SMTPConnectError:
    send_email(465)
