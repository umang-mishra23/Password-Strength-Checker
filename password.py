import re

def check_password_strength(password):
    if len(password) <= 8:
        return "Weak: Too short!"
    if not re.search(r"\d", password):
        return "Weak: No numbers!"
    if not re.search(r"[A-Z]", password):
        return "Weak: No uppercase letters!"
    if not re.search(r"[!@#$%^&*]", password):
        return "Weak: No special characters!"
    return "Strong Password!"

password = input("Enter a password: ")
print(check_password_strength(password))
