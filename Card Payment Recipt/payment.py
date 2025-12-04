
def confirmation_alert(user_name, user_card, payment_amount):
    alert = "transaction alert".center(60).title()
    print(user_card)
    hidden_card = user_card.split()
    for i in range(0, len(hidden_card) - 1):
        hidden_card[i] = "xxxx"
        
    
    print(f"{alert}\nMr. {user_name}, your A/C {" ".join(hidden_card)} debited by {payment_amount} BDT")
    