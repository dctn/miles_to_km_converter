from tkinter import *

windows= Tk()
windows.minsize(width=500, height=400)

# Label
my_label = Label(text="I am stranger",font=("Arial",20,'bold'))
my_label.grid(column=1 , row= 1)

my_label1 = Label(text="I am stranger",font=("Arial",20,'bold'))
my_label1.grid(column=3 , row= 1)
my_label1.config(pady=75)



# Button
# def button_func():
#     print("set")
#     my_label.config(text='button got clicked')

def button_show():
    user_input = entry.get()
    my_label.config(text=str(user_input))

button = Button(text="click me", command=button_show)
button.grid(column=2 , row=2)


# Entry

entry = Entry()
entry.grid(column=4 ,row=3)
entry.config()





windows.mainloop()