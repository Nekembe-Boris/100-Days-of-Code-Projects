from tkinter import *

def converter():
    miles = input.get()
    converted_value = 1.61 * float(miles)
    converted_label.config(text=converted_value)


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=100)



input = Entry(width=15, highlightbackground="blue", highlightthickness=1)
input.place(x=100, y=20)

mile_label = Label(text="Miles", font= ("Century Gothic", 15, "bold"))
mile_label.place(x=200, y=15)

equal_label = Label(text="is equal to", font=("Century Gothic", 12))
equal_label.place(x=10, y=70)

converted_label = Label(text="0", font= ("Century Gothic", 13, "bold"))
converted_label.place(x=130, y=72)

km_label = Label(text="KM", font=("Century Gothic", 15, "bold"))
km_label.place(x=210, y=70)

button = Button(text="Calculate", width=10, command=converter)
button.place(x=105, y=130)


window.mainloop()