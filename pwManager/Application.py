# Application

class Application:
    application = ""
    password = ""
    username = ""
    email = ""

    def __init__(self, a, p, u, e):
        self.application = a
        self.password = p
        self.username = u
        self.email = e

    def setapplication(self, a):
        self.application = a

    def setpassword(self, p):
        self.password = p

    def setusername(self, u):
        self.username = u

    def setemail(self, e):
        self.email = e

    def __str__(self):
        str1 = "" + self.application + ", " + self.password + ", " + self.username + ", " + self.email
        return str1
