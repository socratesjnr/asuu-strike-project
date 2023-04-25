import os
import smtplib
import imghdr
from email.message import EmailMessage

MY_EMAIL = input("Enter sender email address: ")
MY_PASSWORD = input("Enter sender password or application password: ")

TARGET_EMAIL = input("Enter target email address: ")
