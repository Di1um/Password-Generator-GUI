try:
    from tkinter import *
except ImportError:
    from tkinter import *
import time
import pyperclip
from PassGen import password_gen



def pwgenerator(size=8):
    data = password_gen(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    label_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('Segoe UI', 10, 'bold'),
                             bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(.02)
    gui.update()
    gui.mainloop()


# MainWindow
gui = Tk()
gui.config(bg='#D3D3D3')
gui.title('Password Generator')
width = 600
height = 342
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

# Var
PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(12)

# WindowFrame
Top = Frame(gui, width=width)

Top.pack(side=TOP)
Top.config(bg='#D3D3D3')
Form = Frame(gui, width=width, background="#D3D3D3", )
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)

# Label
label_password = Label(Form, font=('Segoe UI', 13), text="Password", foreground="black", background="#D3D3D3", bd=7)
label_password.grid(row=0, pady=10)
label_strength = Label(Form, font=('Segoe UI', 10, 'bold'), foreground="black", background="white", text="Weak", bd=7,
                       height=1, width=10)
label_strength.grid(row=0, column=3, pady=10, padx=10)
label_pw_size = Label(Form, font=('Segoe UI', 13), text="Size", foreground="black", background="#D3D3D3", bd=7)
label_pw_size.grid(row=2, pady=10)
label_instructions = Label(Bot, width=width, font=('Segoe UI', 12, 'bold'),
                           text="Password Generated to your Clipboard!", foreground="black", background="#D3D3D3", bd=1,
                           relief=SOLID)
label_instructions.pack(fill=X)

# Button
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=200, width=24, sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE,
                foreground="black", background="#D3D3D3", font=(16))
pw_size.grid(row=2, column=1, columnspan=2)


# CopytoClip
def copy_password():
    pyperclip.copy(PASSWORD.get())


Button(Top, text='COPY TO CLIPBOARD', foreground="black", background="#D3D3D3", command=copy_password).pack(pady=5)

btn_generate = Button(Form, text="Generate New Password", width=20, command=lambda: pwgenerator(PW_SIZE))
btn_generate.grid(row=4, column=1, columnspan=2)

gui.resizable(False, False)
gui.mainloop()
