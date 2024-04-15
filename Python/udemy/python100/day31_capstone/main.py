from tkinter import *

import pandas

a = pandas.read_csv('Korean_English.csv')

print(a)

#--ui--

window = Tk()
window.title('Flasgy')

canvas = Canvas()