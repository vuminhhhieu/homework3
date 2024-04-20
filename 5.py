name = "admin"
password = "12345"
tk = input("Username: ")
mk = input("Password: ")
if tk == name and mk == password:
    print("You are logged in, admin")
else:
    print("Wrong username or password")
