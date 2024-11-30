"""
Single Responsibility Principle states that each class should have only single responsibility.
(A class should have one and only one reason to change.
"""


# Wrong Example
class userManager:
    def __init__(self):
        __userName = None
        __userPassword = None

    def acceptUserInformation(self, username, password, age, dob):
        # Accept the user information
        pass

    def authenticateUser(self, username, password):
        # Authenticate the information
        pass

    def updateUserProfile(self, username, newProfileDate):
        # update user profile as per new data
        pass

    def sendNotification(self, email, message):
        # send notification to the user
        pass


# The above code has lot of flaws as it has multiple features in it and change/ bug in one can
# lead to error in whole class which we don't want

# Solution: Instead we can create separate classes for this

class userController:
    def acceptUserInformation(self, username, password, age, dob):
        # This will accept the user information
        pass


class userAuthenticator:
    def authenticateUser(self, username, password):
        # Authenticate the information
        pass


class userProfileManager:
    def updateUserProfile(self, username, newProfileDate):
        # update user profile as per new data
        pass


class emailNotifier:
    def sendNotification(self, email, message):
        # send notification to the user
        pass


"""
Now each class has single well definied responsibility, changes in one will not affect the
other functionality and vice versa
"""
