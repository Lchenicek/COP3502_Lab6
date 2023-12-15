
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encode(password):
    # Takes in a string password
    encoded_password = ""
    for char in password:
        encoded_password += str(int(char) + 3)[-1]

    return encoded_password

def decode(password):
    pass


if __name__ == '__main__':

    # Stores the encoded password
    stored_password = None

    while True:
        print_menu()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password_to_encode = input("Please enter your password to encode: ")
            stored_password = encode(password_to_encode)
            print("Your password has been encoded and stored!")
            print()
        elif menu_option == 2:
            # Not a required check, just didn't want the code to break potentially
            if stored_password != None:
                decoded_password = decode(stored_password)
                print(f"The encoded password is {stored_password}, and the original password is {decoded_password}.")
                print()
            else:
                print("Please encode a password first.")
                print()
        elif menu_option == 3:
            break



