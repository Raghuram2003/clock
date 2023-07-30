import pytz
from datetime import datetime
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Clock")
options=["Europe/London", "Australia/Sydney","Asia/Kolkata","America/New_york","Europe/London","Asia/Tokyo","Europe/Paris"]
def get_time_in_timezone():
    timezone = pytz.timezone(clicked.get())
    local_time = datetime.now(timezone)
    string=local_time.strftime("%H:%M:%S ")
    label.config(text=string)
    label.after(1000,get_time_in_timezone)
clicked=StringVar()
clicked.set(options[2])
font_style=("ds-digital",80)
drop = ttk.OptionMenu( root , clicked,*options )
drop.pack()
label=Label(root,font=font_style,background="black",foreground="cyan")
label.pack(anchor='center')
get_time_in_timezone()

root.mainloop()
