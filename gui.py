#! /usr/bin/python

from Tkinter import *

class Application(Frame):

    def say_hi(self):
        print 'hello world'

    def createWidgets(self):

        self.parent.title("Checkers")

#        self.columnconfigure(1, weight=1)
 #       self.columnconfigure(3, pad=7)
  #      self.rowconfigure(3, weight=1)
   #     self.rowconfigure(5, pad=7)

        self.hi = Button(self)
        self.hi['text'] = 'Hello'
        self.hi['command'] = self.say_hi
        self.hi.grid(row=1, column=2)

        self.QUIT = Button(self)
        self.QUIT['text'] = "Quit"
        self.QUIT['fg'] = "red"
        self.QUIT['command'] = self.quit
        self.QUIT.grid(row=3, column=2)

        self.canvas = Canvas(self, width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)
        self.canvas.create_rectangle(50, 20, 150, 80, fill="#476042")
        self.canvas.create_rectangle(65, 35, 135, 65, fill="yellow")
        self.canvas.create_line(0, 0, 50, 20, fill="#476042", width=3)
        self.canvas.create_line(0, 100, 50, 80, fill="#476042", width=3)
        self.canvas.create_line(150,20, 200, 0, fill="#476042", width=3)
        self.canvas.create_line(150, 80, 200, 100, fill="#476042", width=3)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.parent = master
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
