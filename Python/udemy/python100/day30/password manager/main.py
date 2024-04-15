from tkinter import *
from tkinter import messagebox
from genpass import gen_pass
import pyperclip
import json

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

    new_data = {
        input_website:{
            "email": input_username, 
            "password": input_password,
            }
        }
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
        try:
            with open('data.json', 'r') as data:
                json_data = json.load(data)
        except (ValueError, FileNotFoundError):
            with open('data.json', 'w') as data:
                json.dump(new_data, data, indent = 4)
        else:
            json_data.update(new_data)
            with open('data.json', 'w') as data:
                json.dump(json_data, data, indent = 4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- PASSWORD Finder ------------------------------- #

def password_search():
    try:
        with open('data.json', 'r') as file_data:
            json_dictionary = json.load(file_data)
            keyword = entry_website.get().title()
    except FileNotFoundError:
        messagebox.showerror(title='error!', message=f"No file available. Please enter at least one data.")
    else:
        if keyword in json_dictionary:
            information_website = json_dictionary[keyword]
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_username.insert(0, information_website['email'])
            entry_password.insert(0, information_website['password'])
            pyperclip.copy(information_website['password'])
            messagebox.showinfo("Search Success", f"Your password for {keyword} : {information_website['password']} \nhas been copied to your clipboard.\n\nCtrl+V to paste.")
        else:
            messagebox.showerror(title='error!', message=f"You don't have any saved data on {keyword}")

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
entry_website = Entry(width=ONE_COLUMN_WIDTH)
entry_website.focus()
entry_website.grid(column=1, row=1)

#button "Website search"
website_search_button = Button(highlightthickness=0, width=14, text= "Search", command = password_search)
website_search_button.grid(column=2, row=1)


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