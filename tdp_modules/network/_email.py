import smtplib
import ssl


class email_client:
    """
    An emailing client using google's SMTP server.
    """
    def __init__(self,
                 sender,
                 password,
                 port=465):
        self.sender = sender
        self.password=password
        self.port=port

    def __authenticate__(self):

        context = ssl.create_default_context()

        self.server = smtplib.SMTP_SSL("smtp.gmail.com",
                                       self.port, context=context)

        self.server.login(self.sender, self.password)

        return self

    def send_message(self,
                     message,
                     receivers
                     ):

        self.__authenticate__()
        self.server.sendmail(self.sender, receivers, message)
