from pwManager.Application import *
from pwManager.AllApplications import *

obj = Application("a", "p", "u", "e")

obj1 = AllApplications("name")

print(obj1)
obj1.__add__(obj)
print(obj1)
print(obj.password)
obj.setpassword("pe")
print(obj.password)
print(obj.username)


