from tkinter import *
from pwManager.main import *


def button_showaction():
    showwindow = Tk()
    showwindow.title("t")
    showwindow.mainloop()


window = Tk()
window.title("PWManager")
window.geometry("200x250")

applicationlist = Listbox(window)
showbutton = Button(window, text="show PW", command=button_showaction)

y = 1
for x in range(len(allApplications)):
    applicationlist.insert(y, allApplications.__getitem__(x).application)
    y += 1

applicationlist.pack()
showbutton.pack()
window.mainloop()
