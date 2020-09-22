from tkinter import *
from pwManager.main import *


def button_showaction():

    showwindow = Tk()

    global app
    for z in range(len(allApplications)):
        if allApplications.__getitem__(z).application == applicationlist.get(applicationlist.curselection()):
            app = z
            break

    application = Label(showwindow, text=allApplications.__getitem__(app).application)
    password = Label(showwindow, text=allApplications.__getitem__(app).password)
    username = Label(showwindow, text=allApplications.__getitem__(app).username)
    email = Label(showwindow, text=allApplications.__getitem__(app).email)

    application.pack()
    password.pack()
    username.pack()
    email.pack()

    showwindow.title(allApplications.__getitem__(app).application)
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
