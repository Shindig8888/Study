from tkinter import *
from tkinter import messagebox
from genpass import gen_pass
import pyperclip

TWO_COLUMN_WIDTH = 36
ONE_COLUMN_WIDTH = 20

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    #import password generator(from genpass.py), printout password to entry_password, copy to clipboard with popup
    password_generated = gen_pass()
    entry_password.insert(0, password_generated)
    pyperclip.copy(password_generated)
    messagebox.showinfo("Copy Success", "Your password has been copied to your clipboard.\n\nCtrl+V to paste.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    #get inputs, if there is empty field: popup error, if not: popup confirmation
    input_website = entry_website.get().title()
    input_username = entry_username.get()
    input_password = entry_password.get()

    input_data = f"{input_website} | {input_username} | {input_password}\n"
    input_list = {'Website':input_website, 'Email':input_username, 'Password':input_password}
    empty_list = []
    for (key, value) in input_list.items():
        if len(value) == 0:
            empty_list.append(key)
    printdata = "\n".join(empty_list)

    #message box
    if len(input_website) == 0 or len(input_username) == 0 or len(input_password) == 0:
        messagebox.showerror(title='error!', message=f'You have following empty fields.:\n\n{printdata}')
    else:
        is_ok = messagebox.askokcancel(title=input_website, message=f'These are the details entered:\n\nEmail: {input_username}\nPassword: {input_password}\nIs it ok to save?')
    
    if is_ok==True:
        with open('data.txt', 'a') as data:
            data.write(input_data)
        entry_website.delete(0, END)
        entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(highlightthickness=0, width=200, height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column=1,row=0)

#label "Website"
label_website = Label(text = "Website:")
label_website.grid(column=0,row=1)

#entry "Website"
entry_website = Entry(width=TWO_COLUMN_WIDTH)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)


#label "Email/Username"
label_username = Label(text = "Email/Username:")
label_username.grid(column=0,row=2)

#entry "Email/Username"
entry_username = Entry(width=TWO_COLUMN_WIDTH)
entry_username.insert(0,'hindig8888@proton.me')
entry_username.grid(column=1, row=2, columnspan=2)


#label "password"
label_password = Label(text = "Password:")
label_password.grid(column=0,row=3)

#entry "password"
entry_password = Entry(highlightthickness=0, width=ONE_COLUMN_WIDTH)
entry_password.grid(column=1, row=3)

#button "password gen"
gen_password_button = Button(highlightthickness=0, text= "Generate Password", command = password_generator)
gen_password_button.grid(column=2, row=3)


#button "add"
add_button = Button(text="Add", width=TWO_COLUMN_WIDTH, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



#window.mainloop
window.mainloop()