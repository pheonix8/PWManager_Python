from pwManager.AllApplications import *

obj = Application("a", "p", "u", "e")

print(obj.password)
obj.setpassword("pe")

allApplications = []

allApplications.append(obj)

for obj in allApplications:
    print(obj.application, obj.password)

