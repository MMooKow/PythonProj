#Secret Password
#
#User enters a password and gets access or denial.

password = ""

while password != "secret":
    password = input("Please enter the password: ")

    if password != "secret":
        print("ACCESS DENIED!!!")
        continue
    else:
        print("Access granted")

input("Press the enter key to exit...")
