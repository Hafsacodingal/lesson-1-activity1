from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Photo Album")
window.geometry("500x500")

# Heading
Label(window,
      text="My Photo Album",
      font=("Arial",16,"bold")).pack(pady=10)

# Open Image
img = Image.open("photo.png")
img = img.resize((250,250))
photo = ImageTk.PhotoImage(img)

# Show Image
Label(window,image=photo).pack()

# Function
def show_photo():

    messagebox.showinfo("Photo Album","This is my favorite photo!")

    top = Toplevel()
    top.title("Photo Details")
    top.geometry("300x150")

    Label(top,text="Photo Name: My Photo").pack(pady=10)
    Label(top,text="Size: 250 x 250").pack()
    Label(top,text="Created using Tkinter").pack()

# Button
Button(window,
       text="View Details",
       command=show_photo,
       bg="green",
       fg="white").pack(pady=20)

window.mainloop()