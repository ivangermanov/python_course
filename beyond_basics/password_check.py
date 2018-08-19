correct_password = "python123"
password = input("Enter password: ")
name = input("Enter first name: ")
surname = input ("Enter surname: ")

while correct_password != password:
    password = input("Enter password again: ")

message = "Hello, %s %s, you have successfully logged in." %(name, surname)
print(message)