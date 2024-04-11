from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=160, height=120)

entry = Entry(width=10)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=1,row = 0)

lalbel_Miles = Label(text="Miles")
lalbel_Miles.grid(column=2, row=0)


lalbel_is_equal_to = Label(text="is equal to")
lalbel_is_equal_to.grid(column=0, row=1)

lalbel_result = Label(text="0")
lalbel_result.grid(column=1, row=1)

lalbel_KM = Label(text="Km")
lalbel_KM.grid(column=2, row=1)


def calculation()->str:
    miles = int(entry.get())
    km = round(miles * 1.60934,2)
    lalbel_result.config(text = km)


button = Button(text="Caluclate", command=calculation)
button.grid(column=1,row=2)





window.mainloop()