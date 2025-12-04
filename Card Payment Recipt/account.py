import random

def card_genarate(card):
    
    match card:
        case 4:
            card_number = "4" + "".join(str(random.randint(1, 9)) for _ in range(15))
            card_number = " ".join(card_number[i:i+4] for i in range(0, len(card_number), 4))
            print("Visa Card Successfully Genarated")
            return card_number
        case 5:
            card_number = "5" + "".join(str(random.randint(1, 9)) for _ in range(15))
            card_number = " ".join(card_number[i:i+4] for i in range(0, len(card_number), 4))
            print("Master Card Successfully Genarated")
            return card_number

def create_account():
    
    print("Welcome To Card Account Creation Center\n\n")
    
    user_name = input("Enter Your Name: ")
    user_card = ""
    
    while True:
        choice = input("Which Card Do you want to Get?\n1. Visa Card\n2. Master Card\nEnter Your Choice: ")
        
        match choice:
            case "1":
                user_card = card_genarate(4)
                break
            case "2":
                user_card = card_genarate(5)
                break
            case _:
                print("Invalid Input. Please Try Again.")
        
    return user_name, user_card