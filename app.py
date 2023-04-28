from tkinter import *
import openpyxl

base = Tk()
base.geometry('500x500')
base.title("Registration Form")

labl_0 = Label(base, text = "Registration Form", width = 20, font = ("bold", 20))
labl_0.place(x = 90, y = 53)
labl_1 = Label(base, text = "Full Name", width = 20, font = ("bold", 10))
labl_1.place(x = 80, y = 130)
entry_1 = Entry(base)
entry_1.place(x = 240, y = 130)
labl_2 = Label(base, text = "Email", width = 20, font = ("bold", 10))
labl_2.place(x = 68, y = 180)
entry_2 = Entry(base)
entry_2.place(x = 240, y = 180)
labl_3 = Label(base, text = "Gender", width = 20, font = ("bold", 10))
labl_3.place(x = 70, y = 230)
varbl = IntVar()
Radiobutton(base, text = "Male", padx = 5, variable = varbl, value = 1).place(x = 235, y = 230)
Radiobutton(base, text = "Female", padx = 20, variable = varbl, value = 2).place(x = 290, y = 230)
labl_4 = Label(base, text = "Age", width = 20, font = ("bold", 10))
labl_4.place(x = 70, y = 280)
entry_3 = Entry(base)
entry_3.place(x = 240, y = 280)

def save_data():
    wb = openpyxl.load_workbook('Sheet.xlsx')
    sheet = wb.active
    row = [entry_1.get(), entry_2.get(), varbl.get(), entry_3.get()]
    sheet.append(row)
    wb.save('Sheet.xlsx')
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    varbl.set(0)
    entry_3.delete(0, END)

Button(base, text = "Submit", width = 20, bg = 'black', fg = 'white', command = save_data).place(x = 180, y = 380)
base.mainloop()