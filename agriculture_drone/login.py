from tkinter import *

def register_user():
	phone_info=phone.get()
	password_info=password.get()

	file=open("phonelog"+".txt","w")
	file.write(phone_info+"\n")
	file.write(password_info)
	file.close()

	phone_entry.delete(0,END)
	password_entry.delete(0,END)

	Label(screen1,text="Registration Sucess",fg="green",font=("calibri",11)).pack()
def register():
	global screen1
	screen1=Toplevel(screen)
	screen1.title("Register")
	screen1.geometry("300x250")

	global phone
	global password
	global password_entry
	global phone_entry

	phone=StringVar()
	password=StringVar()

	Label(screen1,text="Please enter details below").pack()
	Label(screen1,text="").pack()
	Label(screen1,text="Phone Number * ").pack()
	phone_entry=Entry(screen1,textvariable=phone)
	phone_entry.pack()
	Label(screen1,text="Password * ").pack()
	password_entry=Entry(screen1,textvariable=password)
	password_entry.pack()
	Label(screen1,text="").pack()
	Button(screen1,text="Register",width=10,height=1,command=register_user).pack()

def login():
	print("Login Session Started")
def main_screen():
	global screen
	screen=Tk()
	screen.title("EyeVision")
	screen.geometry("500x500")
	screen.iconbitmap(r'plant_0VY_icon.ico')
	Label(text="").pack()
	Button(text="Login",height="2",width="30",command=login).pack()
	Label(text="").pack()
	Button(text="Register",height="2",width="30",command=register).pack()

	screen.mainloop()
main_screen()