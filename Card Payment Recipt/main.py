import account, payment

print("Card Payment Recipt System\n")

card_issued = False 
payment_status = False

while not payment_status:
    if not card_issued:
        print("You don't have a Card to continue your payment.\nLet me redirect you to create an Account.")
        user_name, user_card = account.create_account()
        card_info = {"user_name": user_name, "user_card": user_card}
        card_issued = True
    else:
        print("You have made a purchese.\n")
        purchese_amount = int(input("Enter the Amount of the Purchese: "))
        payment.confirmation_alert(user_name, user_card, purchese_amount)
        payment_status = True
    