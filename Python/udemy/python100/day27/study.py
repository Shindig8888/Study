import tkinter

window = tkinter.Tk()

window.title("My first GUI program.")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#label
my_label = tkinter.Label(text = "I am a label.".title(), font = ("Arial", 24, "bold"))
my_label['text'] = 'New Value'
my_label.config(text = 'New Text')
# my_label.pack() #스크린에 띄우기
my_label.grid(column=1,row = 1)


# button

# button = tkinter.Button(text = 'Click Me', command = button_clicked)
# # button.pack()

# entry

input = tkinter.Entry(width = 10)
input.grid(column=4, row = 3)
def button_input():
    my_label.config(text = input.get().title())

button = tkinter.Button(text = 'Click Me', command = button_input)
# button.pack()
button.grid(column = 2,row = 2)

#layout manager
#pack()
#place()
#grid()

new_button = tkinter.Button(text = "new button".title())
new_button.grid(column=3,row=1)










window.mainloop()