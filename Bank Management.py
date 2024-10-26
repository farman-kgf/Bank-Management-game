print ("This is a simple Bank Management, number based game")

print ("RULES")
print("Can insert money one time")
print("Can widrowal money 3 times")
print("Have to complet spending money in 3 widroals")

user_name = input("WHAT IS YOUR NAME : ")


credit= float(input("How much money you want to credit : "))

if credit <= 5:
    print ("You have to put at least $5")
    credit= float(input("How much money you want to credit : "))

if credit >= 6:
    print("Amount has been credited")
    spending1 = float(input("How much money you want to spend in first transetion : "))

    remaning_amount_after_spending1 = credit-spending1

    print("Amount left = ", remaning_amount_after_spending1)

    if remaning_amount_after_spending1 > 0:
        print("Last transection was sussceful but there is some amount remaning")
        spending2 = float(input("How much money you want to spend in secound transetion : "))

        remaning_amount_after_spending2 = remaning_amount_after_spending1-spending2
        print("Amount left = ",remaning_amount_after_spending2)

        if remaning_amount_after_spending2 > 0:
            print("Last transection was sussceful but there is some amount remaning")
            spending3 = float(input("How much money you want to spend in third transetion : "))

            remaning_amount_after_spending3 = remaning_amount_after_spending2-spending3
            print("Amount left = ",remaning_amount_after_spending3)

            if remaning_amount_after_spending3 > 0:
                print("Amount left > 0")
                print("DO YOU WANT TO PLAY AGAIN" , user_name)
                user_playagain = input("yes/no")
            
            elif remaning_amount_after_spending3 == 0:
                                print("Amount left = 0")
                                print ("YOU WIN THANKS FOR PLAYING",user_name)
                                print("DO YOU WANT TO PLAY AGAIN" , user_name)
                                user_playagain = input("yes/no")
        
        elif remaning_amount_after_spending2 == 0:
                                print("Amount left = 0")
                                print ("YOU WIN THANKS FOR PLAYING",user_name)
                                print("DO YOU WANT TO PLAY AGAIN" , user_name)
                                user_playagain = input("yes/no")

        elif remaning_amount_after_spending2 == 0:
                print("Amount left = 0")
                print ("YOU WIN THANKS FOR PLAYING",user_name)
                print("DO YOU WANT TO PLAY AGAIN" , user_name)
                user_playagain = input("yes/no")

                if user_playagain == "yes":
                    credit= float(input("How much money you want to credit", user_name , " : "))

                elif user_playagain == "no":
                    print ("THENKS FOR CHOUSING US ONCE")