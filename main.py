import tkinter as tk

root =tk.Tk()
root.title("Miles To Kilometer Converter")
root.minsize(280,200)

miles_label= tk.Label(root,text="miles",font=("Arial",10,))
miles_label.place(x=190,y=68)

km_label= tk.Label(root,text="KM",font=("Arial",10,))
km_label.place(x=190,y=100)

is_equal_label=tk.Label(root,text="is equal to",font=("Arial",10,))
is_equal_label.place(x=40,y=100)

km_final= tk.Label(root,text="   ",font=("Arial",10,))
km_final.place(x=110,y=100)

miles_entry = tk.Entry(root,width=10)
miles_entry.place(x=110,y=70)

def button_clicked():
    distance_in_miles = int(miles_entry.get())
    distance_in_km = distance_in_miles * 1.60934
    km_final.config(text= round(distance_in_km,2))

calculate_button=tk.Button(root,text="Calculate",font=("Arial",10,),command=button_clicked)
calculate_button.place(x=120,y=130)

root.mainloop()
