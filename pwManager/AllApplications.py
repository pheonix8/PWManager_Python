from pwManager.Application import *


class AllApplications:
    name = ""
    allApplications = []

    def __init__(self, n):
        self.name = n

    def __sizeof__(self):
        return self.allApplications

    def __add__(self, other):
        self.allApplications.append(other)
