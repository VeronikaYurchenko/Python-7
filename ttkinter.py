# Import Module
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry('400x500')

# Information List
datas = []

# Add Information
def add():
	global datas
	datas.append([Name.get(),Number.get(),comment.get(1.0, "end-1c")])
	update_book()

# View Information
def view():
	Name.set(datas[int(select.curselection()[0])][0])
	Number.set(datas[int(select.curselection()[0])][1])
	comment.delete(1.0,"end")
	comment.insert(1.0, datas[int(select.curselection()[0])][2])

# Delete Information
def delete():
	del datas[int(select.curselection()[0])]
	update_book()

def reset():
	Name.set('')
	Number.set('')
	comment.delete(1.0,"end")

# Update Information
def update_book():
	select.delete(0,END)
	for n,p,a in datas:
		select.insert(END, n)

# Add Buttons, Label, ListBox
Name = StringVar()
Number = StringVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

Label(frame, text = 'Имя', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=30).pack()

Label(frame1, text = 'Номер телефона.', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()

Label(frame2, text = 'Комментарии', font='arial 12 bold').pack(side=LEFT)
comment = Text(frame2,width=30,height=10)
comment.pack()

Button(root,text="Добавить",font="arial 12 bold",command=add).place(x= 100, y=270)
Button(root,text="Посмотреть",font="arial 12 bold",command=view).place(x= 100, y=310)
Button(root,text="Удалить",font="arial 12 bold",command=delete).place(x= 100, y=350)
Button(root,text="Сбросить",font="arial 12 bold",command=reset).place(x= 100, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

# Execute Tkinter
root.mainloop()
