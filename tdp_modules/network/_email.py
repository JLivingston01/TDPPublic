import smtplib
import ssl


class EmailClient:
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
        self.server=None

    def __authenticate__(self):
        """
        Authentication method for email client.

        Returns
        -------
        SELF.

        """
        context = ssl.create_default_context()

        self.server = smtplib.SMTP_SSL("smtp.gmail.com",
                                       self.port, context=context)

        self.server.login(self.sender, self.password)

        return self

    def send_message(self,
                     message,
                     receivers
                     ):
        """
        Send message to receivers from client.

        Parameters
        ----------
        message : Str
            Body and subject of message.
        receivers : List or Str
            Recipient email addresses.

        Returns
        -------
        None.

        """

        self.__authenticate__()
        self.server.sendmail(self.sender, receivers, message)
