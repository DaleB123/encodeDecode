# Dale Bittner encoder edited by Jay Irby
def encode(number):
    original = str(number)
    new = ""
    for char in original:
        new += str(int(char) + 3)
    return new

def decode(new_pass):
    original_pass = ''
    for i in new_pass:
        original_pass += str((int(i)-3))
    return original_pass
def main():
    running = True
    while running:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == '2':
            try:
                print(f"The encoded password is {password} and the original password is {decode(password)}.\n")
            except:
                print("No decoder function found or no password to decode")
        elif option == '3':
            quit()

if __name__ == "__main__":
    main()
