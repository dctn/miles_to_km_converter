from tkinter import *

font = ("Arial",20,"normal")

app_screen = Tk()
app_screen.minsize(width=400,height=200)

miles_entry = Entry()
miles_entry.grid(column=2, row=1)

miles_label = Label(text="miles", font=font)
miles_label.grid(column=3 ,row=1 )
miles_label.config(padx=10)

is_equal_label = Label(text="is equal to", font=font)
is_equal_label.grid(column= 1, row=2)

ans_label = Label(text=0, font=font)
ans_label.grid(column=2,row=2)
ans_label.config(pady=10)

km_label = Label(text="km", font=font)
km_label.grid(column=3, row=2)
def calculate_func():
    miles = float(miles_entry.get())
    ans = miles * 1.609
    ans_label.config(text=round(ans,2))

cal_button = Button(text='calculate',command=calculate_func)
cal_button.grid(column=2, row=3)




app_screen.mainloop()