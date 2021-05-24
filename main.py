# login exercise
usernames = ["Mikayla", "Liesl", "Ashley", "Kyle", "KJ"]
passwords = ["0159", "2587", "3369", "0710", "0912"]

x = input("Please enter your username: ")
y = input("Please enter your password: ")
# function to log in
for x1 in range(len(usernames)):
    if x == usernames[x1] and y==passwords[x1]:
        found = True
if found == True:
    print("Access granted") # if login successful
else:
    print("Access denied") # if login failed