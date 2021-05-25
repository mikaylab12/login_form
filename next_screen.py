from tkinter import *
window = Tk()
window.title("My Second Form")
window.config(bg="pink")
window.geometry("600x300")

# most comments are for an alternative method
# numbers_entry_1= Entry(window)
# numbers_entry_1.place(x=300, y=70)
# numbers_label = Label(window, text="Enter a list of numbers", bg="pink")
# numbers_label.place(x=120, y=70)
# unsorted_label= Label (frame2, text="Enter a list of numbers", bg="pink")
# unsorted_label.place(x=175, y=50)
# sorted_label = Label(frame2)
# sorted_label.place(x=75, y=100)
# heading
second_heading= Label(window, text="Sorting in Chronological order", bg="pink", font=("Helvetica 20 bold"))
second_heading.place(x=100, y=10)
# labels
numbers_label = Label(window, text="42, 13, 12, 89, 63, 11", bg="pink", font=("Helvetica 20 bold"))
numbers_label.place(x=180, y=70)
myanswer_label=Label(window, bg="pink")
myanswer_label.place(x=250, y=120)

# sorting function
def sorting():
    # x = numbers_entry_1.get().split(",")
    x = [42, 13, 12, 89, 63, 11]
    for j in range (0, 6):
        for i in range(0, 5):
            if (x[i]) > (x[i + 1]):
                swap = x[i]
                x[i] = x[i + 1]
                x[i+1]= swap
        myanswer_label.config(text=x)
# clear function
def clear():
    # numbers_entry_1.delete(0, END)
    myanswer_label.config(text="")
#exit function
def exit():
    window.destroy()
# sort button
sort = Button (window, text="Sort", borderwidth=5, padx=15, pady=10, bg="pink", command=sorting)
sort.place(x=120, y=180)
# clear button
clear_btn = Button(window, text="Clear", borderwidth=5, padx=15, pady=10, bg="pink", command=clear)
clear_btn.place(x=242, y=180)
#exit button
exit_btn = Button(window, text="Exit", borderwidth=5, padx=15, pady=10, bg="pink", command=exit)
exit_btn.place(x=370, y=180)

window.mainloop()