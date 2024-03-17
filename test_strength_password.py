import pyfiglet
def test_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = not any(char.islower() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_char_error = not any(char in '_@$' for char in password)
    
    if length_error:
        return "Weak: Password length should be at least 8 characters"
    elif lowercase_error or uppercase_error or digit_error or special_char_error:
        return "Weak: Password should include lowercase, uppercase, numbers, and special characters"
    else:
        return "Strong: Password meets the strength criteria"
def main():
        banner = pyfiglet.figlet_format("Snoopy")
        print(banner)
        print("           By Usama Ishtiaq \n      ")
        print("[+] This tool helps you to check the strength of your password.\n")

        while True:
             password = input("Enter your password: ")
             strength_result = test_password_strength(password)
             print(strength_result)
             if "Strong" in strength_result:
                break  
if __name__ == "__main__":
    main()
