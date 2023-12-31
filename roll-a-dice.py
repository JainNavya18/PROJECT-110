import random

response = "y"

while response == "y":
   
    dice_value = random.randint(1, 6)

    print("---------")
    
    if dice_value == 1:
        print("|       |")
        print("|   0   |")
        print("|       |")
    elif dice_value == 2:
        print("| 0     |")
        print("|       |")
        print("|     0 |")
    elif dice_value == 3:
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
    elif dice_value == 4:
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
    elif dice_value == 5:
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
    elif dice_value == 6:
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")

    print("---------")

    
    response = input("Roll again? (y/n): ")

print("Thanks for playing! Goodbye!")
