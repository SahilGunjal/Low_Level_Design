from abc import abstractmethod, ABC

"""
Dependency Inversion: High-level modules should not depend on low-level modules; both
should depend on abstractions.
"""


class GmailClient:
    def sendEmail(self, emailAddress, message):
        # logic to send the email using gmail API
        print("mail sent")


class EmailService:
    def __init__(self):
        self.gmailClient = GmailClient()

    def sendEmail(self, emailAddress, message):
        self.gmailClient.sendEmail(emailAddress, message)


# Here the emailService (high level module) depends totally on the low level module (gmailClient)
# there is the tight coupling between the client, which we definitely don't want because in future
# if we extend the functionality and we want to use outlook API then we have to change the code
# this violates the DIP.

# Solution -> create the interface and take it's reference

class EmailClient(ABC):
    @abstractmethod
    def sendEmail(self, emailAddress, message):
        pass


class GmailClient(EmailClient):
    def sendEmail(self, emailAddress, message):
        # logic to send the email using gmail API
        print("mail sent")


class OutlookClient(EmailClient):
    def sendEmail(self, emailAddress, message):
        # logic to send the email using outlook API
        print("mail sent")


class EmailService:
    def __init__(self, eClient):
        self.mailClient = eClient

    def sendEmail(self, emailAddress, message):
        self.mailClient.sendEmail(emailAddress, message)


emailClient = GmailClient()
# emailClient = OutlookClient()
emailService = EmailService(emailClient)
emailService.sendEmail("abc@example.com", "Thank you for the registration")

# This way we can easily choose the client we want to use and even in future we can extend it
# for example, yahooClient, etc.
# Email service depends on the EmailClient abstraction and not the class directly.
