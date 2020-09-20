from pwManager.Application import *

obj = Application("a1", "p1", "u1", "e1")
ob2 = Application("a2", "p2", "u2", "e2")
ob3 = Application("a3", "p3", "u3", "e3")
allApplications = [obj, ob2, ob3]

print(allApplications.__getitem__(0).username)
print(obj.password)