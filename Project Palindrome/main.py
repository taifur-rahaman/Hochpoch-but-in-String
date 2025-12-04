
print("Project Palindrome\n\n")

def checkPalindrome(user_text):
    palin_check = user_text.replace(" ", "").lower()
    if palin_check == palin_check[::-1]:
        return True
    else:
        return False

def makePalindrome(user_text):
    palin_check = user_text.replace(" ", "").lower()
    if palin_check == palin_check[::-1]:
        return user_text
    else:
        reverse_text = user_text[::-1]
        reverse_text = reverse_text.replace(reverse_text[0], "")
        palin_text = user_text + reverse_text
        return palin_text.lower()

while True:
    choice = input("1. Check Palindrome\n2. Make Palindrome\n0. Exit\nEnter Your Choice: ")
    
    match choice:
        case "1":
            user_text = input("Enter Text: ")
            if checkPalindrome(user_text):
                print(f"{user_text} is Palindrome")
            elif not checkPalindrome(user_text):
                print(f"{user_text} is not a Palindrome")
        case "2":
            user_text = input("Enter Text: ")
            palin_text = makePalindrome(user_text)
            print(f"Palindrome of {user_text} is {palin_text.title()}")
        case "0":
            print("Exiting the Program\nGoodbye!")
            break
        case _:
            print("Invalid Input. Please Try Again.")