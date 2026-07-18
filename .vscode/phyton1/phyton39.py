from tkinter import *

window = Tk()
window.title("Personal Bio Form")
window.geometry("600x600")
window.configure(bg="lightblue")

# Heading
heading = Label(window,
                text="Personal Bio Form",
                font=("Arial",16,"bold"),
                bg="skyblue",
                fg="black",
                width=30)
heading.pack(pady=10)

# Labels
Label(window,text="Name",bg="lightblue").place(x=50,y=70)
Label(window,text="Father Name",bg="lightblue").place(x=50,y=110)
Label(window,text="Age",bg="lightblue").place(x=50,y=150)
Label(window,text="Gender",bg="lightblue").place(x=50,y=190)
Label(window,text="Class",bg="lightblue").place(x=50,y=230)
Label(window,text="Hobby",bg="lightblue").place(x=50,y=270)
Label(window,text="City",bg="lightblue").place(x=50,y=310)

# Entry Boxes
e1 = Entry(window,width=30)
e1.place(x=170,y=70)

e2 = Entry(window,width=30)
e2.place(x=170,y=110)

e3 = Entry(window,width=30)
e3.place(x=170,y=150)

e4 = Entry(window,width=30)
e4.place(x=170,y=190)

e5 = Entry(window,width=30)
e5.place(x=170,y=230)

e6 = Entry(window,width=30)
e6.place(x=170,y=270)

e7 = Entry(window,width=30)
e7.place(x=170,y=310)

# Function
def show_bio():
    bio = "PERSONAL BIO\n\n"
    bio += "Name: " + e1.get() + "\n"
    bio += "Father Name: " + e2.get() + "\n"
    bio += "Age: " + e3.get() + "\n"
    bio += "Gender: " + e4.get() + "\n"
    bio += "Class: " + e5.get() + "\n"
    bio += "Hobby: " + e6.get() + "\n"
    bio += "City: " + e7.get()

    result.config(text=bio)

# Button
Button(window,
       text="Show Bio",
       command=show_bio,
       bg="green",
       fg="white").place(x=250,y=360)

# Result Label
result = Label(window,
               text="",
               bg="white",
               justify=LEFT,
               width=45,
               height=10,
               anchor="nw")
result.place(x=80,y=400)

window.mainloop()