import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    self.quitButton = tk.Button(self, text='Sluit', command = self.quit)
    self.frame = tk.LabelFrame(self, text = "Smiley-O-Meter", height = 100, width = 300)
    self.smiley_choices = tk.StringVar()
    self.smiley_choices.set('Blij Zo-zo Sikkeneurig')
    self.smileyChoice = tk.Listbox(self.frame, listvariable = self.smiley_choices)

    self.frame.grid()
    self.quitButton.grid(sticky=tk.S)
    self.smileyChoice.grid()

app = Application()
app.master.title('Aan de slag met Python')
app.mainloop()
