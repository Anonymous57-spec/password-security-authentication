from password_checker import check_password_strength
from auth_system import hash_password, verify_password

print("=== Password Security System ===")

password = input("Create password: ")
print(check_password_strength(password))

hashed = hash_password(password)

login = input("Enter password: ")

if verify_password(hashed, login):
    print("Login Successful ")
else:
    print("Wrong Password ")
