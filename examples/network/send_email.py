"""Example of email class implementation"""
import datetime as dt
import logging
import os
from dotenv import load_dotenv
from tdp_modules.network import EmailClient

def send_email(message,sender,receivers,password,port) -> None:
    """
    A function to use the email_client class.

    Returns
    -------
    None.
    """
    email_client_ = EmailClient(sender = sender,
                                 port=port,
                                 password=password)
    email_client_.send_message(message=message,
                               receivers=receivers)


def main():
    """
    The main method of this example.

    Returns
    -------
    None.

    """
    logging.info("Script began at %s",
        dt.datetime.strftime(dt.datetime.today(),"%Y-%m-%d %H:%M:%S"))


    load_dotenv(".env",override=True)

    sender= 'jay.python.development@gmail.com'
    receivers = 'jay.s.livingston@gmail.com'
    port = 465  # For SSL

    password = os.environ.get("EMAIL_PASS")

    today = dt.datetime.strftime(dt.datetime.today(),"%Y-%m-%d %H:%M:%S")
    message = f"""\
    Subject: Test {today}\n

    Automated message test on {today}."""

    send_email(message=message,sender=sender,
               receivers=receivers,password=password,port=port)


    logging.info("Script finished at %s",
        dt.datetime.strftime(dt.datetime.today(),"%Y-%m-%d %H:%M:%S"))



if __name__=="__main__":

    main()
