from tkinter import *
from colorama import *

w = Tk()
w.title("Enter of information")
w.geometry("523x500")
w.iconbitmap(r"icon.ico")
w.configure(background="#012404")

# Set image-background for main window

img = PhotoImage(file="window_background.png")
image_background_main_window = Button(
    w,
    image=img,
    bg = "#012404"
)
image_background_main_window.place(x=0, y=0, relwidth=1, relheight=1)


def inizialization():
	global a11eg, a12eg, a13eg, b1eg, a21eg, a22eg, a23eg, b2eg, a31eg, a32eg, a33eg, b3eg, img
	w_new = Toplevel(w)
	w_new.title("Answer")
	w_new.geometry("600x580")
	w_new.iconbitmap(r"icon.ico")

	# Image-background for other window
	image_background_other_window = Button(
	    w_new,
	    image=img,
	    bg = "#012404"
	)
	image_background_other_window.place(x=0, y=0, relwidth=1)


	try:
		a11 = float(a11eg.get())
		a12 = float(a12eg.get())
		a13 = float(a13eg.get())
		b1 = float(b1eg.get())
		
		a21 = float(a21eg.get())
		a22 = float(a22eg.get())
		a23 = float(a23eg.get())
		b2 = float(b2eg.get())

		a31 = float(a31eg.get())
		a32 = float(a32eg.get())
		a33 = float(a33eg.get())
		b3 = float(b3eg.get())

		detA = a11*a22*a33+a21*a32*a13+a12*a23*a31-a31*a22*a13-a11*a23*a32-a12*a33*a21

		if detA != 0: # Если detA не равен нулю
			# DetAxn
			detAx1 = b1*a22*a33+b2*a32*a13+a12*a23*b3-b3*a22*a13-b1*a23*a32-a12*a33*b2
			detAx2 = a11*b2*a33+a21*b3*a13+b1*a23*a31-a31*b2*a13-a11*a23*b3-b1*a33*a21
			detAx3 = a11*a22*b3+a21*a32*b1+a12*b2*a31-a31*a22*b1-a11*b2*a32-a12*b3*a21

			# Нахождение xn
			x1 = detAx1/detA
			x2 = detAx2/detA
			x3 = detAx3/detA

			# Вывод
			print(Fore.BLUE)

			print("Результат инициализации вашей матрицы: " + "\n")

			print(f"x1 = {x1}")
			print(f"x2 = {x2}")
			print(f"x3 = {x3}")

			x1label = Label(w_new, text=f'x1 = {x1}', fg="#E4B61D", bg = "#012404", font=(20)).place(relx = .0, rely=.9, relwidth=.33, relheight=.08)
			x2label = Label(w_new, text=f'x2 = {x2}', fg="#E4B61D", bg = "#012404", font=(20)).place(relx = .33, rely=.9, relwidth=.33, relheight=.08)
			x3label = Label(w_new, text=f'x3 = {x3}', fg="#E4B61D", bg = "#012404", font=(20)).place(relx = .6, rely=.9, relwidth=.4, relheight=.08)

		else: # Если detA=0 или другие случаи
			print(Fore.RED)
			print("There are no solutions")
			x1label = Label(w_new, text=f'There are no solutions', bg = "red", font=("Cousine", 20)).place(relx = .0, rely=.85, relwidth=.99999, relheight=.2)

	except ValueError:
		print(Fore.RED)
		print("There are no solutions")
		x1label = Label(w_new, text=f'There are no solutions', bg = "red", font=("Cousine", 20)).place(relx = .0, rely=.85, relwidth=.99999, relheight=.2)

a11eg = StringVar()
a12eg = StringVar()
a13eg = StringVar()
b1eg = StringVar()

a21eg = StringVar()
a22eg = StringVar()
a23eg = StringVar()
b2eg = StringVar()

a31eg = StringVar()
a32eg = StringVar()
a33eg = StringVar()
b3eg = StringVar()

# Creating 12 entety
a11e = Entry(textvariable=a11eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .05, rely = .05, relwidth = .175, relheight = .1)
a12e = Entry(textvariable=a12eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .3, rely = .05, relwidth = .175, relheight = .1)
a13e = Entry(textvariable=a13eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .55, rely = .05, relwidth = .175, relheight = .1)
b1e = Entry(textvariable=b1eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .8, rely = .05, relwidth = .175, relheight = .1)

a21e = Entry(textvariable=a21eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .05, rely = .25, relwidth = .175, relheight = .1)
a22e = Entry(textvariable=a22eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .3, rely = .25, relwidth = .175, relheight = .1)
a23e = Entry(textvariable=a23eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .55, rely = .25, relwidth = .175, relheight = .1)
b2e = Entry(textvariable=b2eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .8, rely = .25, relwidth = .175, relheight = .1)

a31e = Entry(textvariable=a31eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .05, rely = .45, relwidth = .175, relheight = .1)
a32e = Entry(textvariable=a32eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .3, rely = .45, relwidth = .175, relheight = .1)
a33e = Entry(textvariable=a33eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .55, rely = .45, relwidth = .175, relheight = .1)
b3e = Entry(textvariable=b3eg, bg = "#555555", fg = "orange", font=(20)).place(relx = .8, rely = .45, relwidth = .175, relheight = .1)

button = Button(text="Inizialization!", bg="black", fg="cyan", font=("Veles", 10), command = inizialization).place(relx=.5, rely=.65, anchor="c")

w.mainloop()
