import random

number = int(input("Enter the number of friends joining (including you):\n"))
friends = {}

if number < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number):
        name = input()
        friends[name] = 0
    bill = int(input("Enter the total bill value:\n"))
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky == "Yes":
        who = random.choice(list(friends.keys()))
        print(f"{who} is the lucky one!")
        to_pay = round((bill / (len(friends)-1)), 2)
        for k, v in friends.items():
            if k == who:
                pass
            else:
                friends[k] = to_pay
    else:
        print("No one is going to be lucky")
        to_pay = round((bill / len(friends)), 2)
        for i in friends:
            friends[i] = to_pay
            
    print(friends)
  
