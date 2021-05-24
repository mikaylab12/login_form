# converting main.py into tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("600x300")
root.configure(bg="skyblue")
root.title("Login Form")
# tkinter frame in box
frame = Frame(root, width=550, height=200, bg ="#80ccff" )
frame.place(x=25, y=50 )
# heading
heading_label = Label(root, bg="skyblue", text="Enter Your Credentials", font=("Helvetica", 25, "bold"))
heading_label.place(x=120, y=25)
# username label and entry
username_label = Label (frame, text="Enter Username:", bg="#80ccff")
username_label.place(x=120, y=50)
username_entry = Entry(frame)
username_entry.place(x=270, y=50)
# password label and entry
password_label = Label (frame, text="Enter Password:", bg="#80ccff")
password_label.place (x=120, y=100)
password_entry = Entry(frame, show="*")
password_entry.place(x=270, y=100)
# function for logging in
def login():
    usernames = ["Mikayla", "Liesl", "Ashley", "Kyle", "KJ"]
    passwords = ["0159", "2587", "3369", "0710", "0912"]
    found = False
    for x1 in range(len(usernames)):
        if username_entry.get() == usernames[x1] and password_entry.get() == passwords[x1]:
            found = True
    if found == True:
        messagebox.showinfo("Login Successful", "Access Granted!") # if details are entered correctly, can log in
        root.destroy()
        import next_screen
    else:
        messagebox.showinfo("Login Failed", "You have entered your \ndetails in incorrectly!") # if details are entered incorrectly , login will fail
# clear function
def clear():
    password_entry.delete(0, END)
    username_entry.delete(0, END)
#exit function
def exit():
    root.destroy()

# enter button
login_btn = Button(frame, text="Login", borderwidth=5, padx=20, pady=10, bg="#80ccff", command=login)
login_btn.place(x=150, y=150)
# clear button
clear_btn = Button(frame, text="Clear", borderwidth=5, padx=20, pady=10, bg="#80ccff", command=clear)
clear_btn.place(x=250, y=150)
#exit button
exit_btn = Button(frame, text="Exit", borderwidth=5, padx=20, pady=10, bg="#80ccff", command=exit)
exit_btn.place(x=350, y=150)

root.mainloop()