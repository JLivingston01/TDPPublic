from tdp_modules.network import email_client
import datetime as dt
import logging
from dotenv import load_dotenv
import os

def send_email(message,sender,receivers,password,port) -> None:
    
    email_client_ = email_client(sender = sender,
                                 port=port,
                                 password=password)
    email_client_.send_message(message=message, 
                               receivers=receivers)
    
    return None

def main():
    #logging.basicConfig(filename='logs/email.log', level=logging.INFO)

    logging.info(f'''Script began at 
        {dt.datetime.strftime(dt.datetime.today(),"%Y-%m-%d %H:%M:%S")}''')
        
        
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
    
    
    logging.info(f'''Script finished at 
        {dt.datetime.strftime(dt.datetime.today(),"%Y-%m-%d %H:%M:%S")}''')

    return None

if __name__=="__main__":
    
    main()
